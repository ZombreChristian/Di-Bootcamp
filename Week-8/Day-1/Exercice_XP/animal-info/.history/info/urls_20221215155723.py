from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
     path('',views.index,name='index')
     path('', include('info/templates/posts/animal.html')),
]
