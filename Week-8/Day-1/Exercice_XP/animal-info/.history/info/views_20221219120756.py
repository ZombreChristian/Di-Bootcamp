from django.shortcuts import render

# Create your models here.
content = {
    "animals": [
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
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]
}


#family  function renders family.html template
def family(request):
    context = {
        'page_title' : "Homepage",
        'user' : user,
    }
    return render(request, 'info/homepages.html', context)

# animal function renders anima.html template
def posts(request):
    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'page_title' : "Posts",
        'user' : user,
        'subjects': subjects
    }

    return render(request, 'info/posts.html', context)