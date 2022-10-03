from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()
   pw1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
   pw2 = forms.CharField(label = 'Re-type Password', widget=forms.PasswordInput)
   class Meta:
        model = User
        fields = ('username', 'email')

class UserEditForm(UserCreationForm):
   email = forms.EmailField(label="Edit Email")
   pw1 = forms.CharField(label='Password', widget = forms.PasswordInput)
   pw2 = forms.CharField(label='Re-Type Password', widget = forms.PasswordInput)
   class Meta:
      model= User
      fields = ['email', 'pw1', 'pw2']