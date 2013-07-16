                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # Create your views here.

from foo.models import Foo, Emailer, Login
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.generic.detail import BaseDetailView
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


class EmailView(CreateView):
    template_name = "foo/email_index.html"
    model = Emailer
    success_url = "/foo/"

class EmailList(ListView):
    template_name = "foo/sent_emails.html"
    model = Emailer

class EmailDetails(DetailView):
    
    model = Emailer
    success_url = "foo/email_index.html"

class DeleteEmail(DeleteView):
    model = Emailer
    success_url = "/foo/sent_emails/"

#class LoginView(CreateView):
 #   model = Login
  #  success_url = "foo/login_form.html"


class CreateUser(CreateView):
    model = Login
    success_url = "/foo/"


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/foo/loggedin/")
    else:
        # Show an error page
            return render_to_response("foo/login.html", {FormView},
                              context_instance=RequestContext(request))




def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")



class AboutView(ListView):
    template_name = "foo/about.html"
    model = Foo

class UpdateFoo(UpdateView):
    model = Foo
    success_url = "/foo/"

class DeleteFoo(DeleteView):
    model = Foo
    success_url = "/foo/"

class CreateFoo(CreateView):
    template_name = "foo/create.html"
    model = Foo
    success_url = "/foo/"

class FooList(ListView):

    model = Foo
    paginate_by = 3
    #context_object_name = "foo_list"
    #queryset = Book.objects.filter(publisher__name="Acme Publishing")
    template_name = "foo/foo_list.html"


