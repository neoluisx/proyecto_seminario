#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from captcha.fields import ReCaptchaField

class Fcaptcha(forms.Form):
	captcha=ReCaptchaField(attrs={'theme':'clean'})
class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
class fperfil_modificar(ModelForm):
	contra=forms.CharField(max_length=40,required=True,help_text=False,label="Cambiar Password")
	class Meta:
		model=Perfil
		exclude=['user']
class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Contraseña de confirmación", widget=forms.PasswordInput)
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.username=self.cleaned_data.get("username")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user
