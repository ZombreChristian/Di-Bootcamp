from django.shortcuts import render
from info.models import Animal

# Create your views here.
def index(request):
    animals = Animal.objects.all()
    
    context = {"locataires":animals}
    
    return render(request,'index.html',context)