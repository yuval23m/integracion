from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')
