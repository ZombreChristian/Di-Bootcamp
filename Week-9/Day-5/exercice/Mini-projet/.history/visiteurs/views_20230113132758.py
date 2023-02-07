from django.shortcuts import render

# Create your views here.

def home(request):
    message =''
    return render(request,'base.html')
