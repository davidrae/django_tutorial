from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import *
from foo.views import AboutView
from django.views.generic import TemplateView
from foo.views import UpdateFoo, DeleteFoo, CreateFoo, FooList
from django.views.generic.detail import SingleObjectMixin
from foo.views import EmailView, EmailList, EmailDetails, DeleteEmail, login_view, CreateUser, LoggedIn, logout_view, hello_pdf, my_image
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'helloworld.views.home', name='home'),
    #url(r'^helloworld/', include('helloworld.foo.urls')),

   
    url(r'^foo/$', AboutView.as_view()),
    url(r'^foo/create/$', CreateFoo.as_view()),
    url(r'^foo/delete/(?P<pk>.*)/$', DeleteFoo.as_view()),
    url(r'^foo/foo_list/$', FooList.as_view()),

    url(r'^foo/login/$', login_view),
    url(r'^foo/create_user/$', CreateUser.as_view()),
    url(r'^foo/loggedin/$', login_required(LoggedIn.as_view())),
    url(r'^foo/logout/$', logout_view),
    url(r'^accounts/login/$', login_view),

    url(r'^foo/hello/$', hello_pdf),
    url(r'^foo/image/$', my_image),



    url(r'^foo/email_index/$',EmailView.as_view()),
    url(r'^foo/sent_emails/$',EmailList.as_view()),
    url(r'^foo/sent_emails/(?P<pk>.*)/$',EmailDetails.as_view()),
    url(r'^foo/email_index/delete/(?P<pk>.*)/$', DeleteEmail.as_view()),
    
    url(r'^foo/(?P<pk>.*)/$', UpdateFoo.as_view()),



    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
