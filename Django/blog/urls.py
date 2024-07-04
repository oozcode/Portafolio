from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("agenda/", views.agenda, name="agenda/"),
    path("blog/", views.blog, name="blog"),
    path("servicios/", views.servicios, name="servicios"),
    path("agregar-servicio/",views.agregar_servicio, name="agregar_servicio"),
    path("listar-servicio/",views.listar_servicio, name="listar_servicio"),
    path("modificar-servicio/<id>/",views.modificar_servicio, name="modificar_servicio"),
    path("eliminar-servicio/<id>/",views.eliminar_servicio, name="eliminar_servicio"),
    path("agregar-profesional/",views.agregar_profesional,name="agregar_profesional"),
    path("listar_profesional/",views.listar_profesional,name="listar_profesional"),
    path("modificar_profesional/<id>/",views.modificar_profesional,name="modificar_profesional"),
    path("eliminar_profesional/<id>/",views.eliminar_profesional,name="eliminar_profesional"),
]
