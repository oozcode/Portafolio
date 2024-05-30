from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        
    }
    return render(request,'pages/index.html',context)

def proyectos(request):
    context ={

    }
    return render(request,'pages/proyectos.html',context)

def Agenda(request):
    context={

    }
    return render(request,'pages/Agenda.html',context)
def blog(request):
    context={

    }
    return render(request,'pages/blog.html',context)
def servicios(request):
    context={

    }
    return render(request,'pages/servicios.html',context)

    
