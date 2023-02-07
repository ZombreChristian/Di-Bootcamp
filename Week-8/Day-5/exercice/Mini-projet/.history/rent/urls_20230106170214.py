from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ajouterclient ,name='ajouterclient'),
    path('',views.listeclient,name=''),
    path('show',views.show,name='show'),
]
