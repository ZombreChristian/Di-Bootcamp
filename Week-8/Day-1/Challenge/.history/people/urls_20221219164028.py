from django.urls import path
from . import views

urlpatterns = [
    path('', views.peol),
    path('', include("people.urls")),
]
