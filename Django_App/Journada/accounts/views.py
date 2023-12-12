from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt  
from django import forms
from  .forms import SignUpForm
from django.template import loader 




# Create your views here.

@csrf_exempt 
def register(request):
     form=SignUpForm()
     if (request.method == 'POST'):
          form = SignUpForm(request.POST)
          if (form.is_valid()):
               user_email= form.cleaned_data['user_email']
               username= form.cleaned_data['username']
               password= form.cleaned_data['password']
               nuser=User.objects.create(username=username,password=password,user_email=user_email)
               nuser.save()
               return HttpResponse("Thank you for Registering, we are glad to have you! Welcome to Journada," +username)
     form= SignUpForm()
     template = loader.get_template("registration/signup.html")
     return render(request,"registration/signup.html", {'form': form})