# Create your views here.

from foo.models import Foo
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

