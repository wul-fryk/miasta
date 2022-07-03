from django.forms import ModelForm
from .models import Place
from django.contrib.auth.models import User


class User_form(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']

class Place_form(ModelForm):
    class Meta:
        model = Place
        fields = ['place_location', 'place_name']