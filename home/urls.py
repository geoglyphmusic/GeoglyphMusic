from django.urls import path
from . import views
from .models import Homepage

urlpatterns = [
    path('', views.home, name='Home'),
]
