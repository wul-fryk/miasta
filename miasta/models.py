from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Citizen(models.Model):
    citizen_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # city_belong = 
    # work = 
    # messages = 
    pass

class City(models.Model):
    city_name = models.CharField(max_length=33)
    informations = models.TextField(blank=True, null=True)
    citizens = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.city_name

class Place(models.Model):
    place_location = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    place_name = models.CharField(max_length=250)
    # rating = 
    # opinions = 
    # ovner  =
    # workers = 

    def __str__(self):
        return self.place_name

# class Room(models.Model):
#     pass

# class Message(models.Model):
#     pass