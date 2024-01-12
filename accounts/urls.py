from django.urls import path
from accounts import views


urlpatterns = [
    path("signup/", views.register, name="signup"),
    # path('account/login',views.login,name='login')
]
