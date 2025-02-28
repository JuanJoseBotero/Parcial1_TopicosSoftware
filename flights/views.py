from django.shortcuts import render
from .models import Flight

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def registerPost(request):
    if request.method == 'POST':
        name = request.POST['name']
        itsNacional = request.POST['itsNacional']
        price = request.POST['price']
        Flight.objects.create(name=name, flight_type=itsNacional, price=price)
        print(name, itsNacional, price)
    return render(request, 'index.html')