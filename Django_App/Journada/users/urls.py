from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log_session/',views.log_sesssion,name='Log Session')
   ]
