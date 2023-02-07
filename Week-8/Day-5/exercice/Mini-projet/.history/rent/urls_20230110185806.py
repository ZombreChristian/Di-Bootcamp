from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    path('client/listeclient', views.listeclient ,name='listeclient'),
    path('f',views.ajoutervehicule ,name='ajoutervehicule'),
    path('vehicule/listevehicule', views.listevehicule ,name='listevehicule'),
    path('rent/rental<int:id>/',views.afficher , name='afficher' ),
    path('',views.ajouterlocation ,name='ajouterlocation'),
    
    path('rent/rental', views.location ,name='location'),    
]
