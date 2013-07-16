from django.db import models
from django.forms import ModelForm
from django.shortcuts import render



def search_form(request):
    return render(request, 'login.html')