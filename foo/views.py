# Create your views here.

from foo.models import Foo
from django.views.generic import ListView

class AboutView(ListView):
    template_name = "about.html"
    model = Foo