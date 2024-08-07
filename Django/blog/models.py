from django.db import models
#ooz adminadmin
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    Imagen = models.ImageField(upload_to="servicios",null=True)
    descripcion=models.TextField()
    informacion = models.CharField(max_length=100, default='Valor predeterminado')


    def __str__(self):
        return self.nombre
 
class especialista (models.Model):
    nombre = models.CharField(max_length=50)
    Imagen = models.ImageField()

    def __str__(self):
        return self.nombre

class agendar (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField (max_length=100,unique=True,blank=True,null=True)
    fecha = models.DateField()
    mensaje = models.CharField(max_length=100, default='Valor predeterminado')
    especialista = models.ForeignKey(especialista,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


