
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
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from foo.forms import UserForm, FooForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from cStringIO import StringIO
from reportlab.lib.units import inch



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
    
    #if user is not None and user.is_active and user.is_authenticated() and not 
    #user.is_anonymous():

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
    #form = FooForm()
    model = Foo
    success_url = "/foo/"

def create_foo(request):
    #import pdb;pdb.set_trace()
    
    form = FooForm()
    user = auth.get_user(request)
    #import pdb;pdb.set_trace()
    name = form["name"]
    last_name = form["last_name"]
    dob = form["dob"]





class FooList(ListView):

    model = Foo
    paginate_by = 3
    #context_object_name = "foo_list"
    #queryset = Book.objects.filter(publisher__name="Acme Publishing")
    template_name = "foo/foo_list.html"





def my_image(request):
    current_path = os.path.dirname(__file__)
    banana_path = os.path.join(current_path, "static", "foo", "images", "banana.jpg")
    image_data = open(banana_path, "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")




def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = StringIO()

    # Create the PDF object, using the StringIO object as its "file."
    c = canvas.Canvas(temp)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # move the origin up and to the left
    c.translate(inch,inch)
    # define a large font
    c.setFont("Helvetica", 14)#
    # choose some colors
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
    # draw some lines
    c.line(0,0,0,1.7*inch)
    c.line(0,0,1*inch,0)
    # draw a rectangle
    c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
    # make text go straight up
    c.rotate(90)
    # change color
    c.setFillColorRGB(0,0,0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    c.drawString(0.3*inch, -inch, "Hello World")

    # Close the PDF object cleanly.
    c.showPage()
    c.save()

    # Get the value of the StringIO buffer and write it to the response.
    response.write(temp.getvalue())
    return response

def search_form(request):
    return render(request, 'foo/search_form.html')

def search(request):
    #import pdb;pdb.set_trace()

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            return HttpResponse('Please submit a query shorter than 20 characters.')
        else:
            foo = Foo.objects.filter(name__icontains=q)
            return render(request, 'foo/search_results.html',
                {'foo': foo, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')