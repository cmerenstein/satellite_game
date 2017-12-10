from django.shortcuts import render, redirect
from .models import City
import json
import random

# Create your views here.
def game(request):
	n_cities = len(City.objects.all())
	i = round(random.random()*n_cities)
	city = City.objects.get(id_num=i)
	
	dict = {"city_lat":city.lat, "city_lng":city.lng, "city_name": city.name}
	
	return render(request, 'game.html', dict)
	
def index(request):
	
	return render(request, 'index.html', {})