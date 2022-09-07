from django.shortcuts import render,redirect
from Entrega1MV.models import *
from Entrega1MV.forms import *


# Create your views here.

def home(request):
    return render(request, 'Entrega1MV/index.html')

def userCreate(request):
    if request.method == 'POST':
        userform = UsuarioFormulario(request.POST)
        if userform.is_valid():
            information = userform.cleaned_data

            user = Usuario(
                nombre = information['nombre'],
                apellido = information['apellido'],
                edad = information['edad'],
                username = information['username']
            )
            user.save()
            return redirect('Entrega1MVInicio')
    else:
        userform = UsuarioFormulario()
    return render(request, 'Entrega1MV/userCreate.html',{'userform':userform})

def user_info(request):
    users = Usuario.objects.all()
    return render(request, 'Entrega1MV/user_info.html', {"users" : users})

def busqueda_usuario(request):

    info = {'form':BusquedaUsuarioFormulario()}

    return render(request, 'Entrega1MV/buscar_usuario_post.html',info)

def busqueda_usuario_get(request):

    nombre = request.GET.get('nombre')

    user = Usuario.objects.filter(nombre__icontains=nombre)
    return render(request, 'Entrega1MV/buscar_usuario_get.html',{'user':user})


def topics(request):
    return render(request, 'Entrega1MV/index.html')

def create_topics(request):
    if request.method == 'POST':
        subjectform = SubjectFormulario(request.POST)
        if subjectform.is_valid():
            information = subjectform.cleaned_data
            subject = Subject(
                nombre = information['nombre']
            )
            subject.save()
            return redirect('Entrega1MVInicio')
    else:
        subjectform = SubjectFormulario()
    return render(request, 'Entrega1MV/topicCreate.html',{'subjectform':subjectform})

def busqueda_tema(request):

    info = {'form':BusquedaSubjectFormulario()}

    return render(request, 'Entrega1MV/buscar_tema_post.html',info)

def busqueda_tema_get(request):

    nombre = request.GET.get('nombre')

    subject = Subject.objects.filter(nombre__icontains=nombre)
    return render(request, 'Entrega1MV/buscar_tema_get.html',{'subject':subject})


def posts(request):
    return render(request, 'Entrega1MV/index.html')

def create_posts(request):    
    if request.method == 'POST':
        post_form = PosteoFormulario(request.POST)
        if post_form.is_valid():
            information = post_form.cleaned_data
            posteo = Posteo(
                titulo = information['titulo'],
                fecha_creacion = information['fecha_creacion']
            )
            posteo.save()
            
            return redirect('Entrega1MVInicio')
    else:
        post_form = PosteoFormulario()
    return render(request, 'Entrega1MV/postCreate.html',{'post_form':post_form})

def busqueda_post(request):

    info = {'form':BusquedaPosteoFormulario()}

    return render(request, 'Entrega1MV/buscar_post_post.html',info)

def busqueda_post_get(request):

    titulo = request.GET.get('titulo')

    post = Posteo.objects.filter(titulo__icontains=titulo)
    return render(request, 'Entrega1MV/buscar_post_get.html',{'post':post})
