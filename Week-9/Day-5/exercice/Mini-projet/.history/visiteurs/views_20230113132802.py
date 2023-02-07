from django.shortcuts import render

# Create your views here.

def home(request):
    message ='Bonjour'
    return render(request,'base.html')
