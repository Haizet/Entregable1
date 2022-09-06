from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    username = forms.CharField(max_length=40)

class BusquedaUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)

class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    fecha_creacion = forms.DateField()

    
class SubjectFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)