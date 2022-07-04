from multiprocessing import context
from django.shortcuts import redirect, render
from .models import City, Place
from .forms import Place_form, User_form
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    names = City.objects.all()
    context = {'names':names}
    return render(request, 'miasta/home.html', context)

def city_page(request, pk):
    name = City.objects.get(id=pk)
    place = Place.objects.all()
    context = {'name':name, 'place':place}
    return render(request, 'miasta/city_page.html', context)


def add_place_page(request):
    form = Place_form()
    if request.method == 'POST':
        form = Place_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'miasta/add_place.html', context)


def user_login(request):
    login_user = User_form()


    context = {'login_user':login_user}
    return render(request, 'miasta/login_register.html', context)