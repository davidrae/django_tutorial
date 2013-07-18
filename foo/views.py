
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
from foo.forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas


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




class CreateUser(CreateView):
    model = Login
    success_url = "/foo/"

#@login_required
def login_view(request):
   
    form = UserForm()
    user = auth.get_user(request)
    #import pdb;pdb.set_trace()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
    
    #if user is not None and user.is_active and user.is_authenticated() and not user.is_anonymous():

    if user is None or user.is_anonymous():
        messages.error(request, "Username or password is incorrect")
        return render_to_response("foo/login.html", {'form': form, 'cheese': 'is yellow'},
                              context_instance=RequestContext(request))
        
    #import pdb;pdb.set_trace()
    if user.is_active and user.is_authenticated():
        return HttpResponseRedirect("/foo/loggedin/")

        # Correct password, and the user is marked "active"
        # Redirect to a success page.

        # Show an error page


def logout_view(request):
    #import pdb;pdb.set_trace()
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/foo/login/")



#@login_required(login_url='/foo/login/')
class LoggedIn(ListView):
    #form = Userform()
    model = Login
    success_url = "foo/loggedin"



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



def my_image(request):
    image_data = open("/var/projects/helloworld2/helloworld/foo/static/foo/images/banana.jpg", "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")



def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response