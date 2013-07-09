from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import *
from foo.views import AboutView
from django.views.generic import TemplateView
from foo.views import UpdateFoo, DeleteFoo, CreateFoo, FooList
from django.views.generic.detail import SingleObjectMixin
from foo.views import SampleView


urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'helloworld.views.home', name='home'),
    #url(r'^helloworld/', include('helloworld.foo.urls')),

   
    url(r'^foo/$', AboutView.as_view()),
    url(r'^foo/create/$', CreateFoo.as_view()),
    url(r'^foo/delete/(?P<pk>.*)/$', DeleteFoo.as_view()),
    url(r'^foo/foo_list/$', FooList.as_view()),
    url(r'^foo/(?P<pk>.*)/$', UpdateFoo.as_view()),

    url(r'^foo/index/$',SampleView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
