from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/restaurants.html', context)

def create(request):
    work = request.POST.get(request)
    

def new(request):
    return render(request, 'restaurants/new.html')
