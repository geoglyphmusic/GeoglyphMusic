from django.shortcuts import render
from .models import Album

# Create your views here.
def music(request):
	context = {
		'albums': Album.objects.all()
	}
	return render(request, 'music/music.html', context)
