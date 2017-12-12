from django.shortcuts import render, redirect
from .models import City
import json
import random

# Create your views here.
def game(request):
	cities = []
	for j in range(5):
		n_cities = len(City.objects.all())
		i = round(random.random()*n_cities)
		city = City.objects.get(id_num=i)
		cities.append({'city_lat':city.lat, 'city_lng': city.lng, 'city_name':city.name})
		
	json_data = json.dumps(cities)
	return render(request, 'game.html', {"data":json_data})
	
def index(request):
	
	return render(request, 'index.html', {})