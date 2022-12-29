from django.shortcuts import render
from info.models import Animal

# Create your views here.
def index(request):
    animals = Locataire.objects.all()
    
    context = {"locataires":locataires}
    
    return render(request,'index.html',context)