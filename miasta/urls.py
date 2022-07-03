from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city-page/<str:pk>', views.city_page, name='city-page'),

    path('add_place', views.add_place_page, name='add_place'),
]