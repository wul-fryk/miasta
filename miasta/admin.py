from django.contrib import admin

# Register your models here.
from .models import City, Place
admin.site.register(City)
admin.site.register(Place)