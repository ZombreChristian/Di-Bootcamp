from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    
     path('',views.index,name='index'),
     path('',views.family,name='family')
]
