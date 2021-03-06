from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from trivia.apps.usuario.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("trivia.apps.usuario.urls")),
    url(r'^', include("trivia.apps.preguntas.urls")),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)
