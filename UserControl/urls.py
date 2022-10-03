from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from UserControl.views import edit_user, login_request, register

urlpatterns=[
    path('login/',login_request, name = 'Login'),
    path('register/', register, name = 'Register'),
    path('logout/', LogoutView.as_view(template_name='Entrega1Mv/index.html'), name = 'LogOut'),
    path('edit/', edit_user, name='Edit')
]