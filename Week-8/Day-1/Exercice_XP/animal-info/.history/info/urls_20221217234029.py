#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    
     path('',views.posts, name='posts'),
]
     path('',views.index, name='index'),
     
