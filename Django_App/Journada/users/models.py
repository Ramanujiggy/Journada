from django.db import models
from datetime import datetime

# Create your models here.

#creating user model for database
class User(models.Model):
    user_id=  models.BigAutoField(primary_key=True)
    username= models.CharField(max_length=30, blank=False)
    password= models.CharField(max_length=30, blank=False)
    user_email= models.CharField(max_length=30,blank=False)

#creating session model for  database
class Session(models.Model):
    session_id=models.BigAutoField(primary_key=True)
    date=models.DateField(default=datetime.date.today())
    time=models.TimeField(default=datetime.time.now())
    start_time=models.TimeField(default=datetime.datetime.now()) #the start of the 'duration'





