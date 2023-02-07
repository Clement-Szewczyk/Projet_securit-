from django.shortcuts import render

# Create your views here.


def alarme(request):
    return render(request, 'passage/alarme.html')


def extincteur(request):
    return render(request, 'passage/extincteur.html')


def porte(request):
    return render(request, 'passage/porte.html')


def evac(request):
    return render(request, 'passage/evac.html')


def fume(request):
    return render(request, 'passage/fume.html')


def securite(request):
    return render(request, "passage/securite.html")
