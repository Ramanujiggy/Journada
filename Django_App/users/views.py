from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import User, Session
from django.http import JsonResponse 
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, get_list_or_404
#from django.contrib.auth.models import User 
from django.template import loader 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
from django import forms 
from .forms import TrainingSessionForm 
import json 


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
   


def log_session(request):
          form = TrainingSessionForm
          if (request.method == 'POST'):
               form = TrainingSessionForm(request.POST)
               if(form.is_valid()):
                    training_session=form.save(commit=False)
                    training_session.user=request.user
                    hours_trained= form.cleaned_data["hours_trained"]
                    minutes_trained= form.cleaned_data["minutes_trained"]
                    grappling_type= form.cleaned_data["grappling_type"]
                    date = form.cleaned_data["date"]
                    hours= form.cleaned_data["time"]
                    training_session.save()
                    return redirect('home') #change this to the dashboard view for triaining sessions
               else:
                    return JsonResponse({"errors":form.errors}, status=400) 
          else:
               form=TrainingSessionForm()
          return render(request,"user/create_training_log.html",{'form':form})


@login_required
def dashboard(request, user_id): #returns index of all training sessions and the user 
     sessions=Session.objects.filter(user=request.user)
     return render(request, 'user/view_training_log', {'sessions':sessions})
     def serialize(): #returns all training sessions 
          pass 

     
      