from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt  
from django import forms




# Create your views here.

class SignUpForm(UserCreationForm):
    user_email=forms.CharField(label='Email Address:', max_length=100)
    username=forms.CharField(label='Username:',max_length=30)
    password=forms.CharField(label='Password',max_length=50)
    success_url = reverse_lazy("login")
    template_name="registration/signup.html"

