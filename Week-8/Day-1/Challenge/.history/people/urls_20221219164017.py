from django.urls import path
from . import views

urlpatterns = [
    path('', ),
    path('', include("people.urls")),
]
