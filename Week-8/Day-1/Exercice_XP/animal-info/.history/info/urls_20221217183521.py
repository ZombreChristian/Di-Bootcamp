from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    
     path('/homepages.ht',views.index, name='index'),
     path('',views.posts, name='posts'),
]
