from django.db import models

# Create your models here.

class Actor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

class Pelicula(models.Model):
    titulo=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    #def __str__(self):
    #    return f"{self.nombre} - {self.comision}"

class Serie(models.Model):
    titulo=models.CharField(max_length=50)
    temporadas=models.IntegerField()
    #def __str__(self):
    #    return f"{self.nombre} - {self.apellido}"