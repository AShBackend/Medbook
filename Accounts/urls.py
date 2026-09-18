from django.urls import path
from . import views

app_name = "Accounts"

urlpatterns = [
    
    path("Register", views.Register, name="Register")
    ,
    path("Login", views.Login, name="Login")
    ,
    path("Logout", views.Logout, name="Logout")
    ,
    path("Profile", views.My_Profile, name="Profile")
]