from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.filter(brand__name='Hyunday')
    print(cars)
    return render(request, 'cars.html', { 'cars': cars })

def home(request): 
    return render(request, 'home.html')
