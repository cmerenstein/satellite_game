import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'satellite.settings')

import django
django.setup()

import geopy
from geopy.geocoders import Nominatim
import glob
import shutil
from satellite_game.models import City

geolocator = Nominatim()

image_folder = "satellite_pictures"

cities = {}
for picture in glob.glob(image_folder + "\*PNG"):
	base = (os.path.basename(picture))
	city_name = base.split("_")[0]
	try:
		cities[city_name].append(picture)
	except KeyError:
		cities[city_name] = []
		cities[city_name].append(picture)

i = 0
for city in cities.keys():
	for pic in cities[city]:
		new_name = str(i) + "_" + os.path.basename(pic).split("_", 1)[1]
		print(new_name)
		shutil.copy(pic, "satellite/static/" + new_name)
	
	city_location = geolocator.geocode(city)
	
	c = City(city_name = city, name=str(i), lat=float(city_location.latitude), lng=float(city_location.longitude))
	print(c)
	c.save()
	i += 1