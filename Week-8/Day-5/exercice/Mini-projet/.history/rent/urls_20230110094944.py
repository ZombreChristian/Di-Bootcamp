from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('home', views.home ,name='home'),
    path('',views.ajouterclient ,name='ajouterclient'),
    path('client/listeclient', views.listeclient ,name='listeclient'),
    path('',views.ajoutervehicule ,name='ajoutervehicule'),
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),

    #path('ajouterlocation',views.ajouterlocation ,name='ajouterlocation'),
    #path('location/listelocation', views.listelocation ,name='listelocation'),    
]
