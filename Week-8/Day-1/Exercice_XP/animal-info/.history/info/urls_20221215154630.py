from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
     path('', include('info/templates/posts/family.html')),
     path('', include('info/templates/posts/family.html')),
]
