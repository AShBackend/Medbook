from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [

    path("", views.Home, name="Home")
    ,
    path("Contact", views.Contactus, name="Contact")
    ,
    path("About", views.Aboutus, name="About")
    ,
    path("Services", views.Services, name="Services")
]


