import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.title

    class Meta:
    	ordering = ['-pub_date']
