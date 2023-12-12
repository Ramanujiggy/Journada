from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Session
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
   


def log(request):
          form=LogUserSession()
          if (request.method == 'POST'):
               form = LogUserSessionForm(request.POST)
               if(form.is_valid()):
                    date=form.cleaned_data['date']
                    time=form.cleaned_data['time']
                    date=form.cleaned_data['hours_trained']
                    grappling_type=form.cleaned_data['grappling_type']
               nsession=Session.objects.create


          
          response= "Log a training session here! Session id is % --NOT BUILT--"
          return HttpResponse(response)

def dashboard(request, user_id): #returns index of all training sessions and the user 
     all_sessions=User.object.session_id.order_by(date)
     output=", ".join("training session on:" for s in session_id) 
     return HttpResponse(all_sessions)
