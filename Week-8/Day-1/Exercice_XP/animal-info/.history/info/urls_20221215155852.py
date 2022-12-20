from django.contrib import admin
from django.urls import path


urlpatterns = [
    
     path('',views.animal,name='animal')
     path('',views.index,name='family')
]
