from django.urls import path 
from django.contrib import admin
from django.conf.urls import include 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log',views.log,name='log'),
    #path('search/<int:user_id>', views.search,name='search')
   ]
