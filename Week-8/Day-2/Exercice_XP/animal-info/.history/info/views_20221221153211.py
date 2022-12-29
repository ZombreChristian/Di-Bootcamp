from django.shortcuts import render
from info.models import Locataire

# Create your views here.
def index(request):
    locataires = Locataire.objects.all()
    
    context = {"locataires":locataires}
    
    return render(request,'index.html',context)