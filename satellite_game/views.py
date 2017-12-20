from django.shortcuts import render, HttpResponse
from .models import City, Game
import json
import random

# Create your views here.
def game(request):

    if request.method == "POST":
        thisgame = Game(average_miss = request.POST['average_miss'])
        thisgame.save()
        sum = 0
        n = 0
        for game in Game.objects.all():
            sum += game.average_miss
            n += 1
        mean = sum / n
        return HttpResponse(mean)

    else:
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