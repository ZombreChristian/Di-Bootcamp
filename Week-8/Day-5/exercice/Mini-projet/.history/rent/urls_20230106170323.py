from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ajouterclient ,name='ajouterclient'),
    path('listeclient',views.listeclient,name='listeclient'),
    #path('show',views.show,name='show'),
]
