from django.shortcuts import render, redirect , get_object_or_404
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
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Servicio agregado exitosamente"
        else:
            data["form"] = formulario
    return render(request, "pages/agregar_servicio.html",data)

def listar_servicio(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }
    
    return render(request,"pages/listar_servicio.html",data)

def modificar_servicio(request, id):

    servicios = get_object_or_404(Servicio, id=id)

    data = {
        'form': ServicioForm(instance=servicios)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_servicio")
        else:
            data["form"] = formulario

    return render(request,"pages/modificar_servicio.html",data)

def eliminar_servicio(request,id):
    servicios = get_object_or_404(Servicio, id=id)
    servicios.delete()
    return redirect(to="listar_servicio")