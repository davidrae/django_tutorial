from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import *
from foo.views import AboutView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'helloworld.views.home', name='home'),
    #url(r'^helloworld/', include('helloworld.foo.urls')),

   
    url(r'^foo/', AboutView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
