from django.contrib import admin

# Register your models here.
from .models import Album
from .models import Track

admin.site.register(Album)
admin.site.register(Track)
