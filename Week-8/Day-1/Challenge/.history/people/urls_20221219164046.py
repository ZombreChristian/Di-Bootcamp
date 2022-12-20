from django.urls import path
from . import views

urlpatterns = [
    path('', views.people,name="pe"),
    path('', include("people.urls")),
]
