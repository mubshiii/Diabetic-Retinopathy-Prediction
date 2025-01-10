from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200)

class Doctor(models.Model):

    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    image=models.CharField(max_length=150)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=400)
    phone_no=models.CharField(max_length=1000)
    latitude=models.CharField(max_length=1000,default="")
    longitude=models.CharField(max_length=1000,default="")
    qualification=models.CharField(max_length=500,default="")
    status = models.CharField(max_length=500, default='Unblocked')


class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    image = models.CharField(max_length=450)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=400)
    phone_no = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=1000, default="")
    longitude = models.CharField(max_length=1000, default="")