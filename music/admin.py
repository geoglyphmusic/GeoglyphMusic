from django.contrib import admin

# Register your models here.
from .models import Album
from .models import CompilationTrack

admin.site.register(Album)
admin.site.register(CompilationTrack)
