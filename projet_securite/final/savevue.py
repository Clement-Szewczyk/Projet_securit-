user = student.objects.get(
        email=request.session['user'])

    premon = request.session.get('first_name')
    nom = request.session.get('last_name')

    # créer une variable qui peut être utilisé dans le template final.html
    if user.games_completed == 8:
        phrase = " a validé"
        return render(request, "final/final.html", {'user': user, 'name': premon, 'nom': nom, 'phrase': phrase})
    elif user.games_completed > 8:
        return render(request, "final/triche.html")
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
        if user.games_completed == 8:
            # mettre validate à True
            request.session['validate'] = True
            phrase = " a validé"
            return render(request, "final/final.html", {'user': user, 'name': premon, 'nom': nom, 'phrase': phrase})
        else:
            return render(request, "final/triche.html")