from django.shortcuts import render

def pdr (request):
    return render(request, "PDR/pdr.html")
