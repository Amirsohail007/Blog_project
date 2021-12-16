from django import forms
from django.forms import fields
from .models import Registration, Blog

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['user_name','firstname','lastname','email','password',]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','post']