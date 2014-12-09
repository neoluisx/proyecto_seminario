from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',
    url(r'^temas/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    url(r'^partida/$', crear_partida),
    url(r'^espera/$', sala_espera),
    url(r'^salas/$', ver_salas),
)