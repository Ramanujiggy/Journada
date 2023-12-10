from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse 
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, get_list_or_404
#from django.contrib.auth.models import User 

#views MUST contain http response 



def index(request): #returns all users using qs/data variables and serialization from django core
     all_users= User.objects.all()
     data= serialize("json", all_users, fields =('username','user_email'))
     return HttpResponse(data, content_type="application/json")
  
def search(request, user_id ):#retrieve a specific user 
     try:
          user= User.objects.get(pk=user_id)
          serialized_data=serialize('json',[user], fields=('username','user_email'))
          return HttpResponse(serialized_data)
     except User.DoesNotExist:
          return JsonResponse({"error":"User not found"}, status=404)
   
          


def register(request, username, password, user_email):
     output= "Welcome to Journada, your request has been registered. Your information is below.9"

     return HttpResponse()

def log_sesssion(request, session_id):
          response= "Log a training session here! Session id is % --NOT BUILT--"
          return HttpResponse(response)

def dashboard(request, user_id): #returns index of all training sessions and the user 
     all_sessions=User.object.session_id.order_by(date)
     output=", ".join("training session on:" for s in session_id) 
     return HttpResponse(all_sessions)
