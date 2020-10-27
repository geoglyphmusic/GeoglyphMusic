from django.db import models

# Create your models here.
class Track(models.Model):
	artist = models.CharField(max_length=120)
	album = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	year = models.IntegerField()
	tempo = models.IntegerField()
	key = models.CharField(max_length=20)
	energy = models.IntegerField()
