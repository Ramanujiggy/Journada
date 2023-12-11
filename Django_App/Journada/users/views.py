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
from .forms import RegisterUserForm
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
     form=RegisterUserForm()
     #received_data = json.loads(request.body) #loads the request.body as a json object. 
     #nuser=User(username=received_data['username'],password=received_data['password'],user_email=received_data['user_email'])
     #nuser.save()
     if (request.method == 'POST'):
          form = RegisterUserForm(request.POST)
          if (form.is_valid()):
               user_email= form.cleaned_data['user_email']
               username= form.cleaned_data['username']
               password= form.cleaned_data['password']
               nuser=User.objects.create(username=username,password=password,user_email=user_email)
               nuser.save()
               return HttpResponse("Thank you for Registering, we are glad to have you! Welcome to Journada," +username)
     form= RegisterUserForm()
     template = loader.get_template("users/register.html")
     return render(request,"users/register.html", {'form': form})

def log_sesssion(request, session_id):
          response= "Log a training session here! Session id is % --NOT BUILT--"
          return HttpResponse(response)

def dashboard(request, user_id): #returns index of all training sessions and the user 
     all_sessions=User.object.session_id.order_by(date)
     output=", ".join("training session on:" for s in session_id) 
     return HttpResponse(all_sessions)
