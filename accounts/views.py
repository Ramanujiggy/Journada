from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from .forms import SignUpForm


# Create your views here. test


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
