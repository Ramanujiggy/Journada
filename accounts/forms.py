import sys 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms
#sys.path.append('../users')
#from users.models import User 




# Create your views here.
#using UserCreationForm class, already provies username and password parameters.
class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='Email Address', required=True) 
    #first_name= forms.CharField(label='First Name')
    #last_name = forms.CharField(label='Last Name')
    success_url = reverse_lazy("login")
    


    class Meta:
        model = User
        fields=('first_name','last_name','username','password1','password2', 'email')





class LoginForm(UserCreationForm):
    email=forms.EmailField(label='email',required=True)
    sucess_url = reverse_lazy("home")
    
    
    class Meta:
        model = User
        fields=()