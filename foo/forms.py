from django import forms
from django.forms import ModelForm
from django.shortcuts import render
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form



class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class FooForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget)