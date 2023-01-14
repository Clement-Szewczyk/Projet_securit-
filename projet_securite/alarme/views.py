from django.shortcuts import render

def sound (request):
    return render(request, "alarme/legende.html")

def explication_alarme (request):
    return render(request, "alarme/explication_alarme.html ")
