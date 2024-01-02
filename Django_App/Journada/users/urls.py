from django.urls import path 
from django.contrib import admin
from django.conf.urls import include 
from . import views 

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log_session',views.log_session,name='log_session'),
    #path('search/<int:user_id>', views.search,name='search')
   ]
