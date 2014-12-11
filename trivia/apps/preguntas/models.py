from django.db import models

# Create your models here.

class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	class Meta:
		permissions=(
			("bloques_permisos", "bloques_permisos"),
		)

	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.respuesta_correcta
		
class Respuesta_Inco(models.Model):
	Respuesta_Incorrecta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.Respuesta_Incorrecta