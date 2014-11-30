from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

def registro_view(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado")
	else:
		formulario_registro=fusuario()
	return render_to_response("usuario/registro.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cont']>3:
			capchas=Fcaptcha(request.POST)
			if capchas.is_valid():
				pass
			else:
				datos={'formulario':formulario,'capchas':capchas}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					del request.session['cont']
					return HttpResponseRedirect("/perfil/")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/active/")
			else:
				request.session['cont']=request.session['cont']+1
				aux=request.session['cont']
				estado=True
				mensaje="Error en los datos"+str(aux)
				if aux>3:
					capchas=Fcaptcha()
					datos={'formulario':formulario,'capchas':capchas,'estado':estado,'mensaje':mensaje}
				else:
					datos={'formulario':formulario,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
	else:
		request.session['cont']=0;
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("usuario/perfil.html",{},context_instance=RequestContext(request))

def user_active_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/perfil/")
		else:
			if request.method=="POST":
				us=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=us)
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					us.is_active=True
					us.save()
					return HttpResponseRedirect("/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("usuario/activar.html",{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")


def Pagina_Principal(request):
	return render_to_response("blog/Principal.html",{},RequestContext(request))