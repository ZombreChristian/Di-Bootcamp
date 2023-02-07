from django.shortcuts import render , redirect
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation
from rent.forms import ClientForm, VehiculeForm, LocationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'base.html')

def ajouterclient(request):
    #recuperer et afficher les données
    clients = Client.objects.all()
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = ClientForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            try:  
                form.save()
                messages.success(request, 'client enregistré avec succès')    
                return redirect('listeclient')
                
            except:  
                pass 
         #on reinitialise le formulaire vide avec
            form = ClientForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = ClientForm()
   
    context = {"Clients":clients,"form":form}
    
    return render(request,'rent/ajoutclient.html',context)


def ajouterlocation(request):
    #recuperer et afficher les données
    locations = Location.objects.all()
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = LocationForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            try:  
                form.save()  
                return redirect('listelocation')  
            except:  
                pass 
         #on reinitialise le formulaire vide avec
            form = LocationForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = LocationForm()
   
    context = {"locations":locations,"form":form}
    
    return render(request,'rent/ajoutlocation.html',context)

def rentals(request, id):
    rentals= Location.objects.get(id=id)
    return render(request, "rent/rental.html",  {"rentals": rentals})


def ajoutervehicule(request):
    #recuperer et afficher les données
    vehicule_type = TypeVehicule.objects.all()
    taille = TailleVehicule.objects.all()
    #vehicules = Vehicule.objects.all()
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = VehiculeForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            try:  
                form.save()
                messages.success(request, 'Enregistrement réussi')  
                return redirect('listevehicule')  
            except:  
                pass 
         #on reinitialise le formulaire vide avec
            form = VehiculeForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = VehiculeForm()
   
    context = {"type_vehi":vehicule_type,"taille":taille,"form":form}
    
    return render(request,'rent/ajoutvehicule.html',context)


def listeclient(request):  
    clients = Client.objects.all()  
    return render(request,"rent/listeclient.html",{"clients":clients}) 

def listevehicule(request):  
    vehicules = Vehicule.objects.all()  
    return render(request,"rent/listevehicule.html",{"vehicules":vehicules})  


def listelocation(request):  
    locations = Location.objects.all()  
    return render(request,"rent/listelocation.html",{"locations":locations})  


def afficher(request, id):
    if request.method == 'POST':
        pi = Location.objects.get(pk=id)
      
    else:
        pi = Location.objects.get(pk=id)
   
    return render(request, 'afficher.html', {'client':pi})