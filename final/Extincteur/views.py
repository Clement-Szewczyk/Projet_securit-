from django.shortcuts import render
from random import randrange
from common.models import student


def correct(request):
    return render(request, "Extincteur/correct.html")


def correct2(request):
    return render(request, "Extincteur/correct2.html")


def incorrect(request):
    return render(request, "Extincteur/incorrect.html")


def situation_Extincteur(request):
    user = student.objects.get(email=request.session['user'])
    if user.games_completed == 2:
        a = randrange(1, 5, 1)
        if (a == 1):
            return render(request, "Extincteur/Extincteur1.html")
        if (a == 2):
            return render(request, "Extincteur/Extincteur2.html")
        if (a == 3):
            return render(request, "Extincteur/Extincteur3.html")
        if (a == 4):
            return render(request, "Extincteur/Extincteur4.html")
    else:
        # récipérer les données de la session et les afficher

        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session
        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed

        a = randrange(1, 5, 1)
        if (a == 1):
            return render(request, "Extincteur/Extincteur1.html")
        if (a == 2):
            return render(request, "Extincteur/Extincteur2.html")
        if (a == 3):
            return render(request, "Extincteur/Extincteur3.html")
        if (a == 4):
            return render(request, "Extincteur/Extincteur4.html")


def situation_fume(request):
    user = student.objects.get(email=request.session['user'])
    if user.games_completed == 4:
        return render(request, "Extincteur/fume1.html")
    else:

        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session
        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed

        return render(request, "Extincteur/fume1.html")
