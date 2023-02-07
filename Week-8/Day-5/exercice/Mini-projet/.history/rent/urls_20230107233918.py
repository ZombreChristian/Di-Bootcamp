from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    path('/listeclient', views.listeclient ,name='listeclient'),
    path('ajoutervehicule',views.ajoutervehicule ,name='ajoutervehicule'),
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),
    
]
