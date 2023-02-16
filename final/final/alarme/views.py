from django.shortcuts import render
from common.models import student


def sound(request):
    user = student.objects.get(email=request.session['user'])
    if user.games_completed == 1:
        return render(request, "alarme/legende.html")
    else:

        # ajouter +1 à la variable games_completed et mettre à jour la bdd et la session

        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed
        return render(request, "alarme/legende.html")
