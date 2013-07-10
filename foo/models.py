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


    def send_mail(self):
        
        if self.subject and self.body and self.sender_email:
            send_mail(self.subject, self.body, self.sender_email, ['david.rae@vmsuk.com'])

    def __unicode__(self):
        return "Emailer %s %s" % (self.sender_name, self.sender_email)

        # In reality we'd use a form class
        # to get proper validation errors.
