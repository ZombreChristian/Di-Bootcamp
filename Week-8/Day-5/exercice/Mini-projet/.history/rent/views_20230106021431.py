from django.shortcuts import render
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation
from rent.forms import ClientForm, VehiculeForm, loc

# Create your views here.
def ajouterclient(request):
    #recuperer et afficher les données
    clients = Locataire.objects.all()
    
    
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = LocataireForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            form.save()
         #on reinitialise le formulaire vide avec
            form = LocataireForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = LocataireForm()
   
    context = {"locataires":locataires,"form":form}
    
    return render(request,'index.html',context)
