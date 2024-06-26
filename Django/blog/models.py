from django.db import models
from django.contrib.auth.models import user
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    Imagen = models.ImageField()
    descripcion=models.models.TextField()
 
class especialista (models.Model):
    nombre = models.CharField(max_length=50)
    Imagen = models.ImageField()

class agendar (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=30)
    correo = models.EmailField (max_length=100,unique=True,blank=True,null=True)
    especialista = models.ForeignKey(especialista,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)


