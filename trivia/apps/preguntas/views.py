from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *

#Create your views here.
def registro_tema(request):
	usuario=request.user
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensajes="Error no tiene los permisos necesarios"
		datos={"estadoo":estadoo, "mensajes":mensajes}
		return render_to_response("blog/registro_temas.html",datos, RequestContext(request))
	titulo="Regitro de temas"
	temas=Tema.objects.all()
	if request.method=="POST":
		formulario=ftema(request.POST)
		if formulario.is_valid():
			formulario.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas}
			return render_to_response("blog/registro_temas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=ftema()
	datos={'titulo':titulo,'formulario':formulario,'temas':temas}
	return render_to_response("blog/registro_temas.html",datos,context_instance=RequestContext(request))

def add_pregunta(request,id):
	usuario=request.user
	if not usuario.has_perm("preguntas.add_pregunta"):
		return HttpResponse("usted no tiene este permiso")
	tema=Tema.objects.get(id=int(id))
	titulo="Registrar pregunta para el tema de "+tema.nombre
	titulo2="Registre las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST)
		formulario2=frespuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.tema=tema
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			formulario=fpregunta()
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("blog/preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta()
		formulario2=frespuesta()
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("blog/preguntas.html",datos,context_instance=RequestContext(request))
def add_RespuestaI(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	titulo2="Registre las respuestas"
	if request.method=="POST":
		formulario2=frespuestaI(request.POST)
		if formulario2.is_valid():
			respuestai=formulario2.save(commit=False)
			respuestai.pregunta=pregunta
			respuestai.save()	
			estado=True
			formulario2=frespuestaI()
			datos={'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("blog/respuestasI.html",datos,context_instance=RequestContext(request))
	else:
		formulario2=frespuestaI()
	datos={'titulo2':titulo2,'formulario2':formulario2}
	return render_to_response("blog/respuestasI.html",datos,context_instance=RequestContext(request))
def ver_preguntas(request,id):
	tema=Tema.objects.get(id=int(id))
	preguntas=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema,'preguntas':preguntas}
	return render_to_response("blog/ver_preguntas.html",datos,context_instance=RequestContext(request))

def edit_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	titulo="Editar pregunta"
	titulo2="Editar las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST,instance=pregunta)
		formulario2=frespuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("blog/preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta(instance=pregunta)
		formulario2=frespuesta(instance=respuesta)
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("blog/preguntas.html",datos,context_instance=RequestContext(request))

def eliminar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.delete()
	return HttpResponseRedirect("/tema/edit/"+str(id)+"/")
def crear_partida(request):
	return render_to_response("juego/crear_partida.html",{},RequestContext(request))
def ver_salas(request):
	return render_to_response("juego/unirse_partida.html",{},RequestContext(request))
def sala_espera(request):
	return render_to_response("juego/salaespera.html",{'menu':menu},RequestContext(request))

def agregar_permiso(request):
	per=listageneral
	#pdb.set_trace()
	usuario=request.user
	usuario.permissions.add(per);
	return HttpResponse("/permisos/editar/")

def  permisos(request):
	listapermisos=[]
	if request.user.has_perm("usuario.add_tema"):
		listapermisos.append({"url":"/tema/","label":"Registro Temas"})
	if request.user.has_perm("usuario.bloques_permisos"):
		listapermisos.append({"url":"/permisos/","label":"Permisos"})
	return listapermisos
def mispermisos(request):
	menu=permisos(request)
	usuario=request.user
	if not usuario.has_perm("usuario.add_tema"):
		estadoo=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estadoo, "mensaje":mensaje,"menu":menu}
		return render_to_response("usuario/permisos.html",datos, RequestContext(request))
	usuario=User.objects.all()
	listageneral=[]
	listageneral.append({"id":"usuario.add_tema"})
	listageneral.append({"id":"usuario.bloques_permisos"})
	#pdb.set_trace()

	return render_to_response("usuario/permisos.html", {"usuario":usuario,"menu":menu,"lista":listageneral}, RequestContext(request))
