from common.models import student
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
import bcrypt


def encrypt_cesar(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr((ord(char) - 65 + 5) % 26 + 65)
            else:
                cipher_text += chr((ord(char) - 97 + 5) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text


def register(request):
    # Si la méthode de la requête est POST, traitez le formulaire d'inscription
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # créer un nouvel utilisateur
            entre = student()
            mdp = form.cleaned_data.get('password')
            mdp = encrypt_cesar(mdp)
            entre.email = form.cleaned_data.get('email')
            entre.first_name = form.cleaned_data.get('first_name')
            entre.last_name = form.cleaned_data.get('last_name')
            entre.password = mdp
            entre.birth_date = form.cleaned_data.get('birth_date')
            entre.save()
            # redirect to login page
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'connect/register.html', {'form': form})


def verifconect(username, password):
    entre = student.objects.get(email=username)
    password = encrypt_cesar(password)
    # transforme le mot de passe en string et l'encode en utf-8
    # vérifie si le mot de passe est correct
    if password == entre.password:
        return entre
    else:
        print('mot de passe incorrect')
        return None


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # regarder si la personne qui se connect est le super user
            # vérifier si l'utilisateur est inscrit est un superuser de la bdd User
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return redirect('fin/export')
            else:
                if student.objects.filter(email=email).exists():
                    utilisateur = student.objects.get(email=email)
                    # vérifier si l'utilisateur est inscrit dans la bdd common.student
                    connect = verifconect(username=email, password=password)
                    if connect == None:
                        form.add_error(None, 'mot de passe incorrect')
                    if connect is not None:
                        print(utilisateur, 'is connected')

                        # save les infos de l'utilisateur dans la session
                        request.session['user'] = utilisateur.email
                        request.session['email'] = utilisateur.email
                        request.session['first_name'] = utilisateur.first_name
                        request.session['last_name'] = utilisateur.last_name
                        request.session['validate'] = utilisateur.validated
                        request.session['games_completed'] = utilisateur.games_completed
                        # prit la valeur de la session

                        # rediriger vers la page suivante
                        if utilisateur.games_completed == 0:
                            return redirect('/triangle')
                        if utilisateur.games_completed == 1:
                            return redirect('/alarme')
                        if utilisateur.games_completed == 2:
                            return redirect('/extincteur')
                        if utilisateur.games_completed == 3:
                            return redirect('/porte')
                        if utilisateur.games_completed == 4:
                            return redirect('/extincteur/fume')
                        if utilisateur.games_completed == 5:
                            return redirect('/handi')
                        if utilisateur.games_completed == 6:
                            return redirect('/evacuation')
                        if utilisateur.games_completed == 7:
                            return redirect('/pdr')
                        if utilisateur.games_completed == 8:
                            return redirect('/fin')
                        if utilisateur.games_completed >= 9:
                            utilisateur.games_completed = 0
                            utilisateur.save()
                        return redirect('/fin/triche')
                else:
                    form.add_error(
                        None, 'veuillez vous inscrire ou votre email est incorrect')
    else:
        form = LoginForm()

    return render(request, 'connect/login.html', {'form': form})
