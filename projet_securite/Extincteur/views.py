from django.shortcuts import render

def correct(request):
    return render(request, "Extincteur/correct.html")

def incorrect(request):
    return render(request, "Extincteur/incorrect.html")

def extincteur(request):
    return render(request, "Extincteur/jeu_extincteur.html  ")

def situation(request):
    return render(request, "Extincteur/situation_extincteur.html")