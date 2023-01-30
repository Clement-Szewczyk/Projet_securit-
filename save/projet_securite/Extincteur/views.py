from django.shortcuts import render
from random import randrange

def correct(request):
    return render(request, "Extincteur/correct.html")

def incorrect(request):
    return render(request, "Extincteur/incorrect.html")

def situation_Extincteur(request):
    a = randrange(1, 5, 1)
    if (a==1):
        return render(request, "Extincteur/Extincteur1.html")
    if (a==2):
        return render(request, "Extincteur/Extincteur2.html")
    if (a==3):
        return render(request, "Extincteur/Extincteur3.html")
    if (a==4):
        return render(request, "Extincteur/Extincteur4.html")

def situation_fume(request):
    return render(request, "Extincteur/fume1.html")
    