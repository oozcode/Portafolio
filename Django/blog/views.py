from django.shortcuts import render, redirect , get_object_or_404
from .models import Servicio,especialista
from .models import agendar
from .forms import ServicioForm,ProfesionalForm,AgendarForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    Especialistas = especialista.objects.all()
    data = {
        'Especialistas':Especialistas
    }
    context = {}
    return render(request, 'pages/index.html', data)

def proyectos(request):
    context = {}
    return render(request, 'pages/proyectos.html', context)



def agenda(request):
        data = {
        'form': AgendarForm()
        }
        if request.method == 'POST':
            formulario = AgendarForm()
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Agendar Agregado")
                return redirect(to="pages/servicios.html")
            else:
                data["form"] = formulario
        return render(request, 'pages/agenda.html', data)

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

@permission_required('blog.add_servicio')
def agregar_profesional(request):
    data={
        'form':ProfesionalForm
    }
    if request.method =='POST':
        formulario=ProfesionalForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Especialista agregado exitosamente")
            return redirect(to="listar_profesional")
        else:
            data["form"]=formulario
            
    return render(request,"pages/agregar_profesional.html",data)

@permission_required('blog.add_servicio')
def listar_profesional(request):
 especialistas = especialista.objects.all()
 data={
     'especialistas':especialistas
    }
 return render(request,"pages/listar_profesional.html",data)

@permission_required('blog.add_servicio')
def modificar_profesional(request, id):
    especialistas = get_object_or_404(especialista, id=id)
    data = {
        'form': ProfesionalForm(instance=especialistas)
    }

    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST, instance=especialistas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado exitosamente")
            return redirect(to="listar_profesional")
        else:
            data["form"] = formulario
    return render(request, "pages/modificar_profesional.html", data)

@permission_required('blog.add_servicio')
def eliminar_profesional (request,id):
    especialistas = get_object_or_404(especialista,id=id)
    especialistas.delete()
    messages.success(request,"Eliminado exitosamente")
    return redirect(to="listar_profesional")

  