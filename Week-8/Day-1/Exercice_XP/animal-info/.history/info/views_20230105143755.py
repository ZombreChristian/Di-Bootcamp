from django.shortcuts import render


animals = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
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
families = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]


def home(request):
    context ={
        "animal": animal,
        }
    return render(request, "info/home.html", context)

def family(request, x):
    list_family_animal = []
    for value in tableau["animals"]:
        if value["family"] == x:
            list_family_animal.append(value)
    for val in tableau["families"]:
        if val["id"] == x:
             for va in list_family_animal:
                 va["family"] = val["name"] +" id: "+ str(x)
        context = {
        "list" : list_family_animal,
    }
    return render(request, "info/family.html", context)
def animals(request, y):
    list_animal = []
    for value in tableau["animals"]:
        if value["id"]==y:
            list_animal.append(value)
    for val in tableau["families"]:
        if val["id"] == y:
            for va in list_animal:
                va["family"] = val["name"] +" id: "+ str(y)
    context = {"list":list_animal}
    return render(request, "info/animal.html", context)
    