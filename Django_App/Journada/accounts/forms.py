import sys 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms
sys.path.append('../users')
from users.models import User 




# Create your views here.
#using UserCreationForm class, already provies username and password parameters.
class SignUpForm(UserCreationForm):
    user_email=forms.EmailField(label='Email Address') 
    first_name= forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    success_url = reverse_lazy("login")
    template_name="registration/signup.html"


    class Meta:
        model = User
        fields=('first_name','last_name','username','password1','password2')

