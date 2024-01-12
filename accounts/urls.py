from django.urls import path
from accounts import views


urlpatterns = [
    path("accounts/signup/", views.register, name="signup"),
    # path('account/login',views.login,name='login')
]
