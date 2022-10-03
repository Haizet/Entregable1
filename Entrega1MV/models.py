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
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"



class Subject(models.Model):
    nombre = models.CharField(max_length=40)
    posteos = []

    def __str__(self) -> str:
        return f"Nombre del Tema: {self.nombre}"


class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    mensajes = []

    def __str__(self) -> str:
        return f"Nombre del Post: {self.titulo} - Creado el: {self.fecha_creacion}"


class Mensaje(models.Model):
    body = models.CharField(max_length=5000)
    fecha_creacion = models.DateField
