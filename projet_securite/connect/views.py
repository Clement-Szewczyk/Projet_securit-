from common.models import student
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
import bcrypt
# vue page inscription


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def register(request):
    # Si la méthode de la requête est POST, traitez le formulaire d'inscription
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # créer un nouvel utilisateur
            user = student()
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.password = hash_password(form.cleaned_data.get('password'))
            user.save()
            # redirect to login page
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'connect/register.html', {'form': form})

# regard si c'est le super user


def verifconect(username, password):
    try:
        user = student.objects.get(email=username)
        print(user, 'user1')
        if user.password == password:
            return user
        else:
            print('mot de passe incorrect')
            return None
    except student.DoesNotExist:
        return None


# fonction cryptage mot de passe


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # regarder si la personne qui se connect est le super user

            print(email, password)
            # vérifier si l'utilisateur est inscrit est un superuser de la bdd User
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return redirect('final/export')
            # vérifier si l'utilisateur est inscrit dans la bdd common.student

            user = verifconect(username=email, password=password)
            print(user, 'user2')

            if user == None:
                form.add_error(None, 'Email ou mot de passe incorrect')

            if user is not None:
                print(user, 'is connected')
                # affiché toute les infos de l'utilisateur
                print(user.email, user.password, user.games_completed)
                # save les infos de l'utilisateur dans la session
                request.session['user'] = user.email
                request.session['email'] = user.email
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['validate'] = user.validated
                request.session['games_completed'] = user.games_completed
                # prit la valeur de la session
                print("session")
                print(request.session['user'])
                print(request.session['games_completed'])
                # rediriger vers la page suivante
                if user.games_completed == 0:
                    return redirect('/triangle')
                if user.games_completed == 1:
                    return redirect('/alarme')
                if user.games_completed == 2:
                    return redirect('/extincteur')
                if user.games_completed == 3:
                    return redirect('/porte')
                if user.games_completed == 4:
                    return redirect('/extincteur/fume')
                if user.games_completed == 5:
                    return redirect('/handi')
                if user.games_completed == 6:
                    return redirect('/evacuation')
                if user.games_completed == 7:
                    return redirect('/pdr')
                if user.games_completed == 8:
                    return redirect('/final')
                if user.games_completed >= 9:
                    user.games_completed = 0
                    user.save()
                    return redirect('/final/triche')
    else:
        form = LoginForm()

    return render(request, 'connect/login.html', {'form': form})
