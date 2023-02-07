from django.shortcuts import render

# Create your views here.
def triangle(request):
    return render(request, 'triangle/triangle.html')