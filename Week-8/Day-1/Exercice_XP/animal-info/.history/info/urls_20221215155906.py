from django.contrib import admin
from django.urls import path
from info import 

urlpatterns = [
    
     path('',views.animal,name='animal')
     path('',views.index,name='family')
]
