from django.shortcuts import render
from .forms import Reser

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
            return redirect("index")
    else:
        #si non on initialise un formualire vide
        form = LocataireForm()
    return render(request, 'gestionimo/create_locataire.html', {"form":form})
