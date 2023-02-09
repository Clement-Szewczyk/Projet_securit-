from django.shortcuts import render
from common.models import student

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

# vue page inscription


def register(request):
    # Si la méthode de la requête est POST, traitez le formulaire d'inscription
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # redirect to login page
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'connect/register.html', {'form': form})


# créer une fonction qui vérifie si l'utilisateur est inscrit dans la bdd common.student sans utiliser le module django.contrib.auth
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


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = verifconect(username=email, password=password)
            print(user, 'user2')
            if user is not None:
                print(user, 'is connected')
                # affiché toute les infos de l'utilisateur
                print(user.email, user.password, user.games_completed)
                # save les infos de l'utilisateur dans la session
                request.session['user'] = user.email
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
    else:
        form = LoginForm()
    return render(request, 'connect/login.html', {'form': form})
