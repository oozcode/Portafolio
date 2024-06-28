from django.shortcuts import render, redirect , get_object_or_404
from .models import Servicio
from .forms import ServicioForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required

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

@permission_required('blog.add_servicio')
def agregar_servicio(request):

    data = {
        'form': ServicioForm()
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Agregado")
            return redirect(to="listar_servicio")
        else:
            data["form"] = formulario
    return render(request, "pages/agregar_servicio.html",data)

@permission_required('blog.add_servicio')
def listar_servicio(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }
    
    return render(request,"pages/listar_servicio.html",data)

@permission_required('blog.add_servicio')
def modificar_servicio(request, id):

    servicios = get_object_or_404(Servicio, id=id)

    data = {
        'form': ServicioForm(instance=servicios)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado exitosamente")
            return redirect(to="listar_servicio")
        else:
            data["form"] = formulario

    return render(request,"pages/modificar_servicio.html",data)

@permission_required('blog.add_servicio')
def eliminar_servicio(request,id):
    servicios = get_object_or_404(Servicio, id=id)
    servicios.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect(to="listar_servicio")