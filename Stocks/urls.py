#coding=utf-8

from django.conf.urls import patterns, include, url

#permet d'activer l'administration du site
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StocksV2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^register/$', 'utilisateurs.views.registration', name='registration'),
	url(r'^connexion/$', 'utilisateurs.views.connexion', name='connexion'),
    url(r'^admin/', include(admin.site.urls)),
)
