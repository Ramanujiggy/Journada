from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse 
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, get_list_or_404
#from django.contrib.auth.models import User 
from django.template import loader 
from django.views.decorators.csrf import csrf_exempt 
import json 

#views MUST contain http response 



def index(request): #returns all users 
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
   
@csrf_exempt 
def register(request):
     received_data = json.loads(request.body) #loads the request.body as a json object. 
     nuser=User(username=received_data['username'],password=received_data['password'],user_email=received_data['user_email'])
     nuser.save()
     template = loader.get_template("users/register.html")
     context = {
          'username':received_data['username'], 
          'password': received_data['password'],
          'user_email':received_data['user_email']
     }
     return render(request,"users/register.html", context)

def log_sesssion(request, session_id):
          response= "Log a training session here! Session id is % --NOT BUILT--"
          return HttpResponse(response)

def dashboard(request, user_id): #returns index of all training sessions and the user 
     all_sessions=User.object.session_id.order_by(date)
     output=", ".join("training session on:" for s in session_id) 
     return HttpResponse(all_sessions)
