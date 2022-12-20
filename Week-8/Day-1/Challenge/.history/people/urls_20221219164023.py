from django.urls import path
from . import views

urlpatterns = [
    path('', views),
    path('', include("people.urls")),
]
