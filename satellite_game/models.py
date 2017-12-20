from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length = 256)
	lat = models.FloatField()
	lng = models.FloatField()
	id_num = models.IntegerField()


	def __str__(self):
		return str(self.name)

class Game(models.Model):
    average_miss = models.FloatField()
