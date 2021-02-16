from django.shortcuts import render
from .models import Homepage

# Create your views here.
def home(request):
    context = {
        'homepage': Homepage.objects.filter(active=True).first(),
    }
    return render(request, 'home/home.html', context)
