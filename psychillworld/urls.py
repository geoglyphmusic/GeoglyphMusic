from django.urls import path

from . import views

urlpatterns = [
    path('', views.psychillworld, name='PsyChillWorld'),
]
