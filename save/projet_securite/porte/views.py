from django.shortcuts import render

# Create your views here.
def porte(request):
    return render(request, 'porte/porte.html')