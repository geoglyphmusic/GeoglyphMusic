from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychilldb, name='PsyChillDB'),
]
