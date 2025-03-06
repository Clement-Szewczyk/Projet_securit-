from common.models import student
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
import bcrypt
import hashlib

# fonction qui permet de chiffre le mot de passe en Cesar


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


def hashmdp(password, unsername):
    salt = str(unsername).encode('utf-8')
    password = password.encode('utf-8')
    password = bcrypt.hashpw(password, salt)
    return password

# fonction qui permet d'afficher la page d'inscription


def register(request):
    # Si la méthode de la requête est POST, on traite le formulaire d'inscription
    if request.method == 'POST':
        # On crée un formulaire d'inscription avec les données de la requête
        form = RegisterForm(request.POST)
        # On vérifie que le formulaire est valide
        if form.is_valid():
            # On récupère les données du formulaire en les ajoutant à la base de données
            entre = student()
            mdp = form.cleaned_data.get('password')

            entre.email = form.cleaned_data.get('email')
            entre.first_name = form.cleaned_data.get('first_name')
            entre.last_name = form.cleaned_data.get('last_name')
            # entre.password = encrypt_cesar(mdp)
            entre.password = mdp
            entre.birth_date = form.cleaned_data.get('birth_date')
            # On sauvegarde l'objet dans la base de données
            entre.save()
            # redirection vers la page de connexion
            return redirect('login')
    else:
        # Si la méthode de la requête est GET, on affiche le formulaire d'inscription
        form = RegisterForm()
    return render(request, 'connect/register.html', {'form': form})

# Fonction qui permet de vérifier si l'utilisateur rentre les bonnes informations


def verifconect(username, password):
    print(password)
    # On récupère l'utilisateur dans la bdd
    entre = student.objects.get(email=username)

    # on chiffre le mot de passe rentrer sur la page de connection avec la même fonction que le mot de passe enregistrer dans la bdd
    # On regarde si les deux mots de passe sont identiques
    # mdp = encrypt_cesar(password)
    if password == entre.password:

        # Si oui on retourne l'utilisateur
        return entre
    else:
        # Si non on retourne None
        return None

# Fonction qui affiche la page de connexion


def login(request):
    # Si la méthode de la requête est POST, on traite le formulaire de connexion
    if request.method == 'POST':
        # On crée un formulaire de connexion avec les données de la requête
        form = LoginForm(data=request.POST)
        # On vérifie que le formulaire est valide
        if form.is_valid():
            # On récupère les données du formulaire
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # regarder si la personne qui se connect est le super user
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                # Si oui on vérifie que le mot de passe est correct
                if user.check_password(password):
                    # Si on lance le téléchargement du fichier des résultats
                    return redirect('fin/export')
            else:
                # Si non on vérifie que l'utilisateur est bien dans la bdd common.student
                if student.objects.filter(email=email).exists():
                    # récupérer les infos de l'utilisateur s'il existe
                    utilisateur = student.objects.get(email=email)
                    # vérifier si l'utilisateur est inscrit dans la bdd common.student
                    connect = verifconect(username=email, password=password)
                    if connect == None:
                        # Si non on affiche un message d'erreur (mot de passe incorrect)
                        form.add_error(None, 'mot de passe incorrect')
                    if connect is not None:

                        # Si oui, on save les infos de l'utilisateur dans la session
                        request.session['user'] = utilisateur.email
                        request.session['email'] = utilisateur.email
                        request.session['first_name'] = utilisateur.first_name
                        request.session['last_name'] = utilisateur.last_name
                        request.session['validate'] = utilisateur.validated
                        request.session['games_completed'] = utilisateur.games_completed

                        # rediriger vers la page de en fonction du nombre de jeux terminé
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
                        # si l'utilisateur a qu'il a terminé 9 jeux, ce qui est impossible, on le remet à 0 et on le redirige au début.
                        if utilisateur.games_completed >= 9:
                            utilisateur.games_completed = 0
                            utilisateur.save()
                            return redirect('/triangle')
                else:
                    # Si l'utilisateur n'est pas dans la bdd common.student,
                    # Soit il n'est pas inscrit, soit il a mal noté son email
                    form.add_error(
                        None, 'veuillez vous inscrire ou votre email est incorrect')
    else:
        # Si la méthode de la requête est GET, on affiche le formulaire de connexion
        form = LoginForm()

    return render(request, 'connect/login.html', {'form': form})
