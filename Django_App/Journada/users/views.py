from django.shortcuts import render
from django.http import HttpResponse 



def index(request):
     return HttpResponse("Page not found.")


def register(request):
     return HttpResponse("Hello welcome to Journada!")