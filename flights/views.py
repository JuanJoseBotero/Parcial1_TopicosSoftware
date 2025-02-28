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

def listFlights(request):
    flights = Flight.objects.all()
    return render(request, 'list.html', {'context': flights})

def statistics(request):
    flights = Flight.objects.all()
    promedio = 0
    total = 0
    nacional = 0
    internacional = 0
    for flight in flights:
        total += flight.price
        if flight.flight_type == 'Nacional':
            nacional += 1
        else:
            internacional += 1
    promedio = total / len(flights)
    context = {
        'promedio': promedio,
        'nacional': nacional,
        'internacional': internacional
    }
        
    return render(request, 'statistics.html', {'context': context})