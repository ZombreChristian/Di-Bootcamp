from django.shortcuts import render , redirect
from visiteurs.models import Reservation
from visiteurs.forms import ReservationForm
from  django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    #message ='Bonjour'
    #return HttpResponse(message)
    return render(request,'base.html')


@login_required
def create_reservation(request):
    # test Si la request est une soumission
    if request.method == 'POST':
        #On initialise le formulaire avec les données contenues
        form = ReservationForm(request.POST)
        #test si le formulaire est valide 
        if form.is_valid():
            #On enregistre
            form.save()
            return redirect("home")
    else:
        #si non on initialise un formualire vide
        form = ReservationForm()
    return render(request, 'visiteurs/createReservation.html', {"form":form})
