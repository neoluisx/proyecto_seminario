from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
#from django.contrib import admin
#from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', login_usuario),
    url(r'^registro' , Registro_Usuario),
  )