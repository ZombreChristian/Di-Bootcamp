from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ajouterclient',views.ajouterclient ,name='ajouterclient'),
    path('listecl',views.listeclient,name='listeclient'),
    #path('show',views.show,name='show'),
]