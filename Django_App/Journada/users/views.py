from django.shortcuts import render
from django.http import HttpResponse
from .models import User

#views MUST contain http response 



def index(request):
     return HttpResponse("Page not found.")


def register(request):
     return HttpResponse("Hello welcome to Journada!")

def log_sesssion(request, session_id):
          response= "Log a training session here! Session id is % --NOT BUILT--"
          return HttpResponse(response % session_id)

def dashboard(request, user_id): #returns index of all training sessions and the user 
     all_sessions=User.object.session_id.order_by(date)
     output=", ".join("training session on:" for s in session_id) 
     return HttpResponse(all_sessions)
