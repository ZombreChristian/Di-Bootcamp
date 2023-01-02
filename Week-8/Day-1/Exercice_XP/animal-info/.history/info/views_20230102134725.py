from django.shortcuts import render
from django.http import HttpResponse
from .models import animals

# Create your models here.

#family  function renders family.html template
""" def family(request):
    
    families =[
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]
    context = {
        "families" : families
    }
    return render(request, 'info/family.html',context)

# animal function renders animal.html template
def animal(request):
    
   animals = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2.
            
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
                                {
                                    "id": 3,
                                    "name": "Panther",
                                    "legs": 2,
                                    "weight": 5.67,
                                    "height":4.2,
                                    "speed": 34,
                                    "family": 1 
                                }
    ]

   
   



   context = {
        "animals" : animals
    }
    
   return render(request, 'info/animal.html',context)

 """
 
def listing(request):
    #animaux = ["<li>{}</li>".format(animal['name']) for animal in animals]
    #message = """<ul>{}</ul>""".format("\n".join(animaux))
    context = {
        "animals" : animals
    }
    
    return render(request, 'info/animal.html',context)

def detail(request,id):
    context = {
        "animals" : animals[id]
    }
    id = int(id)
    
    animal
    
    return render(request, 'info/animal.html',context)
