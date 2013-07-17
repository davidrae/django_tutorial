from django import forms
from django.forms import ModelForm
from django.shortcuts import render



def search_form(request):
    return render(request, 'login.html')

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()