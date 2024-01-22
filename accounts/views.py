from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.urls import reverse_lazy
from django.views import generic

# from django.views.decorators.csrf import csrf_exempt
from django import forms
from .forms import SignUpForm
from django.template import loader
from users.models import User
from django.http import HttpResponse

password=S23IB3X2WZ8BWU1P$
# Create your views here.


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")

    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "registration/login.html")
