from django.shortcuts import render
from .models import City
# Create your views here.
def home(request):
    names = City.objects.all()
    context = {'names':names}
    return render(request, 'miasta/home.html', context)

def city_page(request, pk):
    name = City.objects.get(id=pk)
    context = {'name':name}
    return render(request, 'miasta/city_page.html', context)