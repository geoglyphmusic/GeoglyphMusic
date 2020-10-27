from django.shortcuts import render
from .models import Album
from django.shortcuts import get_object_or_404


# Create your views here.
def music(request):
	context = {
		'albums': Album.objects.all()
	}
	return render(request, 'music/music.html', context)

def album(request, album_title):
    album = get_object_or_404(Album, title=album_title)
    context = {
        'album': album
    }
    return render(request, 'music/album.html', context)
