#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
      #path('',views.family, name='family'),
      path('/i',views.animal_detail, name ='animal_detail'),
      
      path('family',views.family, name ='family'),
      #path('id',views.detail, name ='detail'),
    
    
]
     
     
