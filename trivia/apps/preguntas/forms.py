#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import *

class ftema(ModelForm):
	class Meta:
		model=Tema

class fpregunta(ModelForm):
	class Meta:
		model=Pregunta
		exclude=['tema']

class frespuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']
class frespuestaI(ModelForm):
	class Meta:
		model=Respuesta_Inco
		exclude=['pregunta']

