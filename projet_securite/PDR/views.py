from django.shortcuts import render
from common.models import student


def pdr(request):
    user = student.objects.get(email=request.session['user'])
    if request.session['games_completed'] == 7:
        return render(request, "PDR/pdr.html")
    else:
        # récipérer les données de la session et les afficher
        print("session passage")
        print(request.session['user'])
        print(request.session['games_completed'])
        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session

        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed
        print(request.session['games_completed'])
        return render(request, "PDR/pdr.html")
