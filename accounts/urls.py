from django.urls import path
from accounts import views 




urlpatterns =[
    path('registration/signup',views.register,name='signup'),
    
]
