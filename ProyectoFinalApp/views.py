from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import *
from ProyectoFinalApp import *

# Create your views here.
def Profesores_index (request:HttpRequest) -> HttpResponse:
    profesores= Profesores.objects.all()
    return render (request, 'profesores_index.html', {"profesores":profesores})

def inicio (request):
    return render (request,"inicio.html")