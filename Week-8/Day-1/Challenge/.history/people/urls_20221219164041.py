from django.urls import path
from . import views

urlpatterns = [
    path('', views.people,name=),
    path('', include("people.urls")),
]
