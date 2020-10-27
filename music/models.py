from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    label = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album_covers')
    bandcamp = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class CompilationTrack(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    compilation = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album_covers')

    def __str__(self):
        return self.title
