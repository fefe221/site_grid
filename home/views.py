# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')

