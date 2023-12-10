from django.db import models
from datetime import datetime, timedelta
import time 
from django.utils import timezone 
from . import apps 

# Create your models here.

  

#creating user model for database
class User(models.Model):
    """def __init__(self, username:str, password:str, user_email:str,user_id):
        self.user_email = user_email
        self.password = password
        self.username = username"""


    #table definition stuff....
    user_id=  models.BigAutoField(primary_key=True)
    username= models.CharField(max_length=100, blank=False)
    password= models.CharField(max_length=100, blank=False)
    user_email= models.CharField(max_length=100,blank=False)

    def serialize(self): #serializing the data for json web response
        return{
            'user_id': user_id,
            'username': username,
            'user_email': user_email
        }




#creating session model for  database
class Session(models.Model):
    session_id=models.BigAutoField(primary_key=True)
    date=models.DateField(default=timezone.now)
    time=models.TimeField(default=timezone.now)
    hours_trained=models.IntegerField(default=0)
    #adding userID foreign key 
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True) #adding foreign key to associate with user
    #converting user_id to string
    def __str__(self):
        return self.user_id
    


    






