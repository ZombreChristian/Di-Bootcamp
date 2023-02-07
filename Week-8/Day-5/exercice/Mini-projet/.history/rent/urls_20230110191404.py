from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('rent/customer/ajouterclient',views.ajouterclient ,name='ajouterclient'),
    
    path('rent/customer/', views.listeclient ,name='listeclient'),
    
    path('rent/customer/<int:', views.listeclient ,name='listeclient'),
    
    path('f',views.ajoutervehicule ,name='ajoutervehicule'),
    
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),
    
    path('rent/rental/<int:pk>/',views.location , name='location' ),
    
    path('',views.ajouterlocation ,name='ajouterlocation'),
    
    path('rent/rental', views.locations ,name='locations'),    
]
