from django.shortcuts import render
from info.models import Animal,Family

# Create your views here.
def index(request):
    animals = Animal.objects.all()
    families = Family.objects.all()
    
    context = {"animals":animals,
               "families"
               }
    
    return render(request,'index.html',context)