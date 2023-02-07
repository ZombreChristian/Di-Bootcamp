from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    
    path('rr', views.locations ,name='locations'), 
    
    
    path('rent/customer/ajouterclient',views.ajouterclient ,name='ajouterclient'),
    
    path('rent/customer/', views.clients ,name='clients'),
    
    path('rent/customer/<int:pk>', views.client ,name='client'),
    
    path('rent/vehicle/ajoutervehicule',views.ajoutervehicule ,name='ajoutervehicule'),
    
    path('rent/vehicle', views.vehicules ,name='vehicule'),
    
    path('rent/vehicle/<int:pk>',views.vehicule , name='vehicule' ),
    
    path('rent/rental/<int:pk>',views.location , name='location' ),
    
    path('rent/rental/ajouterlocation',views.ajouterlocation ,name='ajouterlocation'),
    
       
]
