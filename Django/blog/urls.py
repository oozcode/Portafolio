from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("agenda/", views.agenda, name="agenda"),
    path("blog/", views.blog, name="blog"),
    path("servicios/", views.servicios, name="servicios"),
]
