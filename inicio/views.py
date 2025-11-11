from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Camiseta

def inicio(request):
    return render(request, "inicio.html")

def otra(request):
    return render(request, "otra.html")

def crear_camiseta(request, club, modelo, talle):

    camiseta = Camiseta(club=club, modelo=modelo, talle=talle)
    camiseta.save()
    
    return render(request, "crear-camiseta.html", {'camiseta': camiseta})

def listar_camisetas(request):

    camisetas = Camiseta.objects.all()
    return render(request, "listar-camisetas.html", {'camisetas': camisetas})
    