from django.shortcuts import render
from info.models import Animal

# Create your views here.
def index(request):
    animal = Animal.objects.all()
    
    context = {"animals":animal}
    
    return render(request,'index.html',context)