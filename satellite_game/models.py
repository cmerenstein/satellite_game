from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length = 256)
	lat = models.FloatField()
	lng = models.FloatField()
	city_name = models.CharField(max_length = 256)
		
	def open_set(self):
		return self.space_set.filter(letter = " ")

