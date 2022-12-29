from django.shortcuts import render
from info.models import Animal

# Create your views here.
def index(request):
    animals = Animal.objects.all()
    
    context = {"animals":animals}
    
    return render(request,',context)