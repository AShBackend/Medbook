from django.db import models
from django.contrib.auth.models import User


class Speciality(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    

class Doctor(models.Model):
    Profile = models.ImageField(upload_to="Image")
    Fullname = models.CharField(max_length=50)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="doctors")
    Pattients = models.IntegerField(default=0)
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Score = models.FloatField(default=0)
    Phone_Number = models.CharField(max_length=20)
    Exprince_Years = models.IntegerField(default=0)
    Bio = models.TextField()

    def __str__(self):
        return self.Fullname


class Reserver(models.Model):
    Name = models.ForeignKey(User, on_delete=models.CASCADE)
    Doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date_Time = models.DateTimeField()
    Reason = models.TextField()

    def __str__(self):
        return self.Name.username