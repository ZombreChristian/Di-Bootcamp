from django.contrib import admin
from django.urls import path
from 

urlpatterns = [
    
     path('',views.animal,name='animal')
     path('',views.index,name='family')
]
