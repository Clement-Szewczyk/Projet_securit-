from django.shortcuts import render
from common.models import student
## import HttpResponse
from django.http import HttpResponse
import csv


def final(request):
    user = student.objects.get(email=request.session['user'])
    premon = request.session.get('first_name')
    nom = request.session.get('last_name')
    email = request.session.get('email')
    valide = request.session.get('validated')

    if user.games_completed < 7 and user.games_completed > 8:
        user.games_completed = 0
        user.save()
        print(user.games_completed)
        return render(request, "final/triche.hml")

    if user.games_completed == 8:
        user.validated = True
        user.save()
        print(user.validated)
        phrase = " a validé"
        return render(request, "final/final.html", {'email': email, 'name': premon, 'nom': nom, 'phrase': phrase})
    else:
        user.games_completed = user.games_completed + 1
        user.save()
        request.session['games_completed'] = user.games_completed
        if user.games_completed == 8:
            # mettre validated à true
            user.validated = True
            user.save()
            print(user.validated)
            phrase = " a validé"
            return render(request, "final/final.html", {'email': email, 'name': premon, 'nom': nom, 'phrase': phrase})
        else:
            user.games_completed = 0
            user.save()
            print(user.games_completed)
            return render(request, "final/triche.html")


def triche(request):
    return render(request, "final/triche.html")


def export(request):
    # récupérer les infos de la bdd student
    # les mettre dans un fichier csv dans des colonnes séparées
    # le télécharger

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow(['email', 'first_name', 'last_name',
                    'validated', 'games_completed'])
    for user in student.objects.all().values_list('email', 'first_name', 'last_name', 'validated', 'games_completed'):
        writer.writerow(user)
    return response
