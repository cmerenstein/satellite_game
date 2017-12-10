from django.shortcuts import render, redirect
from .models import City
from geopy.distance import great_circle
import json
import random
from django.template import RequestContext

# Create your views here.
def game(request):
	n_cities = len(City.objects.all())
	i = round(random.random()*n_cities)
	city = City.objects.get(pk=i)
	
	dict = {'zoom_1': city.name + '_zoom_1.PNG', 'zoom_3': city.name + '_zoom_3.PNG'}
	
	city_location = (city.lat, city.lng)
	dict['city_lat'] = city.lat
	dict['city_lng'] = city.lng
	
	if request.method == 'POST':
		guess = (float(request.POST['lat']), float(request.POST['lng']))
		distance = great_circle(guess, city_location)
		dict['guess_lat'] = float(request.POST['lat'])
		dict['guess_lng'] = float(request.POST['lng'])

		print(distance)
		dict['guessed'] = True
		dict['distance'] = str(distance)
	djson = json.dumps(dict)
	print(djson)
	dict['djson'] = djson
	
	
	
	return render(request, 'game.html', dict)
	
def index(request):

	
	
	return render(request, 'index.html', {})