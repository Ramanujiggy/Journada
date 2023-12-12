from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt  
from django import forms
from  .forms import SignUpForm
from django.template import loader
from users.models import User 
from django.http import HttpResponse



# Create your views here.

#@csrf_exempt 
def register(request):
     form=SignUpForm()
     if (request.method == 'POST'):
          form = SignUpForm(request.POST)
          if (form.is_valid()):
               user_email= form.cleaned_data['user_email']
               username= form.cleaned_data['username']
               password= form.cleaned_data['password2']
               first_name=form.cleaned_data['first_name']
               last_name=form.cleaned_data['last_name']
               nuser=User.objects.create(username=username,password=password,user_email=user_email,first_name=first_name,last_name=last_name)
               nuser.save()
               return HttpResponse("Thank you for registering, we are glad to have you! Welcome to Journada, " + first_name)
     form= SignUpForm()
     #template = loader.get_template("registration/signup.html")
     return render(request,"registration/signup.html", {'form': form})