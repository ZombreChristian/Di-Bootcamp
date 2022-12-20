from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
     path('',views.animal,name='index')
     path('',views.index,name='index')
]
