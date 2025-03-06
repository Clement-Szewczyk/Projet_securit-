from django.shortcuts import render
from common.models import student

# fonction qui permet d'afficher la page du jeu de l'alarme


def sound(request):
    # On récupère l'utilisateur dans la bdd via la session
    user = student.objects.get(email=request.session['user'])
    # Si la variable games_completed est égale à 1 alors on affiche la page
    if user.games_completed == 1:
        return render(request, "alarme/legende.html")
    else:

        # ajouter +1 à la variable games_completed lorsque qu'il arrive pour la première fois sur la page

        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed
        return render(request, "alarme/legende.html")
