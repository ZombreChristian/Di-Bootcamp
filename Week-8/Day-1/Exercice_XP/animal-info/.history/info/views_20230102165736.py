from django.shortcuts import render
from django.http import HttpResponse
from .models import animals
from .models import families
 
def animal_detail(request,id):
    id_an = id
    animal_detail = animals.objects.filter(id=id)
    context = {
        "animal" : animal_detail
    }
    
    return render(request, 'info/detail.html',context)

def family(request):
    
    context = {
        "families" : families
    }
    
    return render(request, 'info/family.html',context)


""" def detail(request,id):
    
    id = int(id)
    context = {
        "animal" : animals[id]
    }
    
    return render(request, 'info/detail.html',context) """
    
     