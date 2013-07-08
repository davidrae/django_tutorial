from django.db import models
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

# Create your models here.
class Foo(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True,
		help_text="put your name here")
	last_name = models.CharField(max_length=10, blank=True)
	dob = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name


