from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	correo=models.EmailField()

	def __unicode__(self):
		return self.usuario.username
	