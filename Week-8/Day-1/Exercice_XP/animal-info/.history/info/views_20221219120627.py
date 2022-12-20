from django.shortcuts import render

# Create your models here.
content = 


# index function renders homepage.html template
def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : user,
    }
    return render(request, 'info/homepages.html', context)

# posts function renders posts.html template
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