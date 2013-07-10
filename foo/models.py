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

    sender_name = models.CharField(max_length = 30, blank = True, null = True, default = "sender", help_text = "put your name here")
    sender_email = models.EmailField(default='david.rae@vmsuk.com')
    subject = models.CharField(max_length=255, help_text='title of the email')
    body = models.TextField(help_text='Content of the email')


    def send_mail(subject, body, sender_email):
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        sender_email = request.POST.get('sender_email', '')
        if subject and body and sender_email:
            try:
                send_mail(subject, body, sender_email, ['david.rae@vmsuk.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/foo/')
        else:
        # In reality we'd use a form class
        # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

            
