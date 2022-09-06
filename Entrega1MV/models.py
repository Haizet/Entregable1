from django.db import models
from django import forms

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    username = models.CharField(max_length=40)
    mensajes = []
    posteos = []
    
    def __str__(self) -> str:
        return super().__str__()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nac = forms.DateField()
    username = forms.CharField(max_length=40)

class Subject(models.Model):
    nombre = models.CharField(max_length=40)
    posteos = []

class SubjectFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)

class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    mensajes = []

class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    fecha_creacion = forms.DateField()

class Mensaje(models.Model):
    body = models.CharField(max_length=5000)
    fecha_creacion = models.DateField
