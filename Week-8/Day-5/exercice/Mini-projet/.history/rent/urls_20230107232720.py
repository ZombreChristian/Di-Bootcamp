from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    path('', views.listeclient ,name='listeclient'),
    
]
