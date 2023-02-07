from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('rent/customer/ajouterclient',views.ajouterclient ,name='ajouterclient'),
    
    path('rent/customer/', views.clients ,name='listeclient'),
    
    path('rent/customer/<int:pk>', views.client ,name='listeclient'),
    
    path('rent/vehicle/ajouter',views.ajoutervehicule ,name='ajoutervehicule'),
    
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),
    
    path('rent/rental/<int:pk>',views.location , name='location' ),
    
    path('',views.ajouterlocation ,name='ajouterlocation'),
    
    path('rent/rental', views.locations ,name='locations'),    
]
