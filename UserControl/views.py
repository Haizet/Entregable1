from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from UserControl.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            pw = data.get('password')

            user = authenticate(username = usuario,password = pw)
            if user is not None:
                login(request,user)
                messages.info(request, "entro")
                return render(request, 'Entrega1MV/index.html')
            else:
                messages.info(request, "No entro")
                return render(request, 'Entrega1MV/index.html')
        else:
            return redirect("Entrega1MV/index.html")

    form = AuthenticationForm()
    return render(request,"UserControl/login.html",{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'Entrega1MV/index.html')
    else:
        form = UserRegisterForm()

    return render(request, "UserControl/register.html",{"form":form})

@login_required
def edit_user(request):

    usuario = request.user
    if request.method == 'POST':
        miformulario = UserEditForm(request.POST)
        info = miformulario.clean_data
        usuario.email = info['email']
        usuario.pw1 = info['password1']
        usuario.pw2 = info['password2']
        usuario.save()
        return render(request, "Entrega1MV/index.html")
    else:
        miformulario = UserEditForm(initial = {'email':usuario.email})
    return render(request, 'UserControl/edit_user.html', {'miformulario':miformulario, 'usuario':usuario})
