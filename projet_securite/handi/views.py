from django.shortcuts import render

# Create your views here.


def handi(request):
    return render(request, "handi/securise.html")
