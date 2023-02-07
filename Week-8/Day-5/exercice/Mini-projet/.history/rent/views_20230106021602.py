from django.shortcuts import render
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation
from rent.forms import ClientForm, VehiculeForm, LocationForm

# Create your views here.
def ajouterclient(request):
    #recuperer et afficher les données
    clients = Client.objects.all()
    
    
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = ClientForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            form.save()
         #on reinitialise le formulaire vide avec
            form = ClientForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = ClientForm()
   
    context = {"Clients":Clients,"form":form}
    
    return render(request,'.html',context)
