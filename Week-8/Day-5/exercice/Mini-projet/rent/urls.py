from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    
    path('rent/listelocation', views.listelocation ,name='listelocation'), 
    
    
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    
    path('rent/customer/', views.listeclient ,name='listeclient'),
    
    path('rent/customer/<int:pk>', views.client ,name='client'),
    
    path('rent/vehicle/ajoutervehicule',views.ajoutervehicule ,name='ajoutervehicule'),
    
    path('rent/vehicle', views.listevehicule ,name='listevehicule'),
    
    path('rent/vehicle/<int:pk>',views.vehicule , name='vehicule' ),
    
    path('rent/rental/<int:pk>',views.location , name='location' ),
    
    path('rent/rental/ajouterlocation',views.ajouterlocation ,name='ajouterlocation'),
    
       
]
