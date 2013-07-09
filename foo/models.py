from django.db import models
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError

# Create your models here.
class Foo(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True,
		help_text="put your name here")
	last_name = models.CharField(max_length=20, blank=True, null=True)
	dob = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class Emailer(models.Model):

	name = models.CharField(max_length=20, blank=True, null=True,
		help_text="put your name here")
	last_name = models.CharField(max_length=10, blank=True)
	dob = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name
'''subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['david.rae@vmsuk.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')'''