import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'satellite.settings')

import django
django.setup()

from satellite_game.models import City

i = 0

with open("simplemaps-worldcities-basic.csv", 'r', encoding='utf-8') as worldcities:
	header = True
	for line in worldcities:
		row = line.split(',')
		if not header:
			pop = float(row[4])
			if pop >= 500000:
				c = City(name=row[0], lat = float(row[2]), lng = float(row[3]), id_num = i)
				c.save()
				i += 1
		else:
			header = False