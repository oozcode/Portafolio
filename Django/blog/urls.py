from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("",views.proyectos,name="proyectos"),
    path("",views.Agenda,name="Agenda"),
    path("",views.blog,name="blog"),
    path("",views.servicios,name="servicios")

    
]
