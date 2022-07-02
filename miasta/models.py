from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=33)
    informations = models.TextField(blank=True, null=True)
    citizens = models.IntegerField(blank=True, null=True)
    # places = 

    def __str__(self):
        return self.city_name

class Place(models.Model):
    place_name = models.CharField(max_length=250)
    # rating = 
    # opinions = 
    # ovner  =
    # workers = 

# class Room(models.Model):
#     pass

# class Message(models.Model):
#     pass