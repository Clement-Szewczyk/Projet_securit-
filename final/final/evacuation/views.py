from django.shortcuts import render
from common.models import student

# Create your views here.


def index(request):
    user = student.objects.get(email=request.session['user'])
    if user.games_completed == 6:
        return render(request, "evacuation/index2.html")
    else:
        # récipérer les données de la session et les afficher

        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session

        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed

        return render(request, "evacuation/index2.html")
