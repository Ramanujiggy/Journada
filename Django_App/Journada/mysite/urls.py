"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView 
from django.contrib.auth import views as auth_views
from  . import settings 
from accounts import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/logout', views.user_logout, name='logout'),
    path("",views.home, name='home'),
    #path('accounts/logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='journada_logout')
    #path('register/', views.register, name='register') 
]
