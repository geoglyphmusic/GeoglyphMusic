from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Homepage(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    video_url = models.CharField(max_length=500, null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.title
