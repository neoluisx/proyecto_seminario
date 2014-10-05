from django.conf.urls import patterns, include, url
from django.contrib import admin
from trivia.apps.usuario.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include("trivia.apps.usuario.urls")),
)
