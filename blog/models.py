import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    abstract = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    date_published = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.title

    class Meta:
    	ordering = ['-date_published']
