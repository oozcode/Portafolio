from django.shortcuts import render
from .models import Servicio
from .forms import ServicioForm

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def proyectos(request):
    context = {}
    return render(request, 'pages/proyectos.html', context)

def agenda(request):
    context = {}
    return render(request, 'pages/agenda.html', context)

def blog(request):
    context = {}
    return render(request, 'pages/blog.html', context)

def servicios(request):
    servicios = Servicio.objects.all()
    data={
        'servicios': servicios
    }
    context = {}
    return render(request, 'pages/servicios.html', data)

def agregar_servicio(request):

    data = {
        'form': ServicioForm()
    }
    context = {}
    return render(request, "pages/agregar.html",data)