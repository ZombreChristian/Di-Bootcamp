from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #message ='Bonjour'
    #return HttpResponse(message)
    return render(request,'base.html')
