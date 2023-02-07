from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    path('client/listeclient', views.listeclient ,name='listeclient'),
    path('ajoutervehicule',views.ajoutervehicule ,name='ajoutervehicule'),
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),

    path('ajouterlocation',views.ajouterlocation ,name='ajoutervehicule'),
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),    
]
