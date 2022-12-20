from django.urls import path
from . import views

urlpatterns = [
    path('', views.people,),
    path('', include("people.urls")),
]
