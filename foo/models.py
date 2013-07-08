from django.db import models

# Create your models here.
class Foo(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True,
		help_text="put your name here")
	last_name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name