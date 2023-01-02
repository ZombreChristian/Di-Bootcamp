#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
      #path('',views.family, name='family'),
      path('',views.listing, name =''),
    
]
     
     
