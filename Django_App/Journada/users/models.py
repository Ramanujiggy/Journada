from django.db import models
from django.conf import settings 
from datetime import datetime, timedelta
import time 
from django.utils import timezone 
from . import apps 

# Create your models here.

  

#creating  custom user model for database
class User(models.Model):
    
    #table definition stuff....
    user_id=  models.BigAutoField(primary_key=True)
    first_name=models.CharField(max_length=100,unique=False)
    last_name=models.CharField(max_length=100,unique=False)
    username= models.CharField(max_length=100, blank=False,unique=True)
    password= models.CharField(max_length=100, blank=False)
    email= models.EmailField(max_length=100,blank=False,unique=True)
    last_login= models.DateTimeField(default=timezone.now)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    USERNAME_FIELD= 'username'

    def serialize(self): #serializing the data for json web response
        return{
            'user_id': user_id,
            'username': username,
            'user_email': email
        }




#creating session model for  database
class Session(models.Model):
    session_id=models.BigAutoField(primary_key=True)
    date=models.DateField(blank=False)
    time=models.TimeField(blank=False)
    hours_trained=models.IntegerField(default=0)
    minutes_trained=models.IntegerField(default=0)
    grappling_type=models.CharField(default='Gi')
    notes = models.TextField(blank=True, null=True)
    #adding userID foreign key 
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True) #adding foreign key to associate with user
    #converting user_id to string
    def __str__(self):
        return self.user_id
    


    






