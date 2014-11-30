from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
#from django.contrib import admin
#from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Pagina_Principal),
    #url(r'^login', login_usuario),
    url(r'^registro' , registro_view),
   # url(r'^user/perfil/$',perfil_view),
   url(r'^login' ,login_view),
    url(r'^logout/$',logout_view),
    url(r'^perfil/$',perfil_view),
    url(r'^active/$',user_active_view),
    #url(r',^media/(?<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
  )