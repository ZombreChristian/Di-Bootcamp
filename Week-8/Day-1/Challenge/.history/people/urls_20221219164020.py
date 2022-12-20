from django.urls import path
from . import views

urlpatterns = [
    path('', vie),
    path('', include("people.urls")),
]
