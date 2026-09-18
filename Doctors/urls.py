from django.urls import path
from . import views

app_name = "Doctors"

urlpatterns = [

    path("Doctor", views.Doctors, name="Doctor")
    ,
    path("Doctors/<int:id>", views.Profiles, name="Profiles")
    ,
    path("Appointments", views.Appointment, name="Appointment")

]
