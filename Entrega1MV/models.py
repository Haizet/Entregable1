from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    username = models.CharField(max_length=40)
    mensajes = []
    posteos = []
    
    def __str__(self) -> str:
        return super().__str__()



class Subject(models.Model):
    nombre = models.CharField(max_length=40)
    posteos = []


class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    mensajes = []



class Mensaje(models.Model):
    body = models.CharField(max_length=5000)
    fecha_creacion = models.DateField
