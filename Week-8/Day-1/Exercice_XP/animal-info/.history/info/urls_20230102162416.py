#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
      #path('',views.family, name='family'),
      path('id/',views.animal_deyta, name ='animal'),
      
      path('family',views.family, name ='family'),
      #path('id',views.detail, name ='detail'),
    
    
]
     
     
