__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

