from django.shortcuts import render
from common.models import student


def pdr(request):
    user = student.objects.get(email=request.session['user'])
    if request.session['games_completed'] == 7:
        return render(request, "PDR/pdr.html")
    else:

        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session

        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed

        return render(request, "PDR/pdr.html")
