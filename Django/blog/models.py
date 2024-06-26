from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    Imagen = models.ImageField
    descripcion=models.CharField(max_length=50)