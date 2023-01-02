#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
      #path('',views.family, name='family'),
      path('',views.listing, name ='listing'),
      path(r'^(?P<id>[0]/',views.detail, name ='detail'),
    
    
]
     
     
