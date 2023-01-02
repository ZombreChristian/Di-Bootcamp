#from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
      path('/x',views.family, name='family'),
      path('animal/x',views.animal, name='animal'),
    
]
     
     
