from django.shortcuts import render
from Entrega1MV.models import *


# Create your views here.

def home(request):
    return render(request, 'Entrega1MV/index.html')

def user_create(request):
    if request.method == 'POST':
        userform = UsuarioFormulario(request.POST)
        if userform.is_valid:
            information = userform.cleaned_data

            user = Usuario(
                nombre = information['nombre'],
                apellido = information['apellido'],
                edad = information['edad'],
                fecha_nac = information['fecha_nac'],
                email = information['email'],
                username = information['username']
            )
            Usuario.save()
    else:
        userform = UsuarioFormulario()
    return render(request, 'Entrega1MV/user_create.html',{'userform':userform})

def user_info(request):
    users = Usuario.objects.all()
    info = {"users" : users}
    return render(request, 'Entrega1MV/user_info.html', info)

def topics(request):
    return render(request, 'Entrega1MV/index.html')

def create_topics(request):
    if request.method == 'POST':
        subjectform = SubjectFormulario(request.POST)
        if subjectform.is_valid:
            information = subjectform.cleaned_data
            subject = Subject(
                nombre = information['nombre']
            )
            subject.save()
    else:
        subjectform = SubjectFormulario()
    return render(request, 'Entrega1MV/user_create.html',{'subjectform':subjectform})

def posts(request):
    return render(request, 'Entrega1MV/index.html')

def create_posts(request):    
    if request.method == 'POST':
        post_form = PosteoFormulario(request.POST)
        if post_form.is_valid:
            information = post_form.cleaned_data
            posteo = Posteo(
                titulo = information['titulo'],
                fecha_creacion = information['fecha_creacion']
            )
            posteo.save()
    else:
        post_form = PosteoFormulario()
    return render(request, 'Entrega1MV/user_create.html',{'post_form':post_form})