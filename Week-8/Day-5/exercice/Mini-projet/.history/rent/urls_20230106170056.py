from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ajouterclient ,name='ajouterclient'),
    path('index',views.index,name='index'),
    path('show',views.show,name='show'),
]
