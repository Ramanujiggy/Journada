from django.shortcuts import render
from django.http import HttpResponse 



def index(request):
     return HttpResponse("Page not found.")


def register(request):
     return HttpResponse("Hello welcome to Journada!")

def log_sesssion(request, session_id):
          response= "Log a training session here! Session id is %"
          return HttpResponse(response % session_id)

def log_view(request, user_id):
          return