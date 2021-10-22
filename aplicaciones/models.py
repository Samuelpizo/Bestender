from django.db import models
from django.db.models.base import Model
from django.utils import timezone


# Create your models here.
class proveedor (models.Model):

    #user= models.ForeignKey(User,on_delete=models.CASCADE)

    codigo = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    gmail = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        texto = " {0} {1} {2} {3} "
        return texto.format(self.nombre,self.telefono,self.gmail,self.direccion)


class producto (models.Model):

    #user= models.ForeignKey(User,on_delete=models.CASCADE)

    codigoPrd = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=30)
    categoria= models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150,default="" )
    cantidadA = models.IntegerField(default=0)
    tipodeTransaccion= models.CharField(max_length=10,default="")
    fecha = models.DateField(default=timezone.now)
    cantidadB= models.IntegerField(default=0) 

    nombreP= models.CharField(max_length=30, default="...")

    class Meta:
        ordering= ['-fecha']
    


    def __str__(self):
        texto = " {0} {1} {2} {3} "
        return texto.format(self.codigoPrd,self.nombre,self.categoria,self.cantidadA)
        



        