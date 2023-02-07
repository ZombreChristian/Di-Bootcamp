from django.shortcuts import render , redirect
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation
from rent.forms import ClientForm, VehiculeForm, LocationForm

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
    locations = Lo.objects.all()
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = ClientForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            try:  
                form.save()  
                return redirect('listeclient')  
            except:  
                pass 
         #on reinitialise le formulaire vide avec
            form = ClientForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = ClientForm()
   
    context = {"Clients":clients,"form":form}

def ajoutervehicule(request):
    #recuperer et afficher les données
    vehicules = Vehicule.objects.all()
    #test si la request est une soumission
    if request.method == 'POST':
        #on initialise le formulaire avec
        form = VehiculeForm(request.POST)
        
        if form.is_valid():
            #on enregitre
            try:  
                form.save()  
                return redirect('listevehicule')  
            except:  
                pass 
         #on reinitialise le formulaire vide avec
            form = VehiculeForm()
    else :
        #sinon on  reinitialise le formulaire vide avec
        form = VehiculeForm()
   
    context = {"Vehicules":vehicules,"form":form}
    
    return render(request,'rent/ajoutvehicule.html',context)


def listeclient(request):  
    clients = Client.objects.all()  
    return render(request,"rent/listeclient.html",{"clients":clients}) 

def listevehicule(request):  
    vehicules = Vehicule.objects.all()  
    return render(request,"rent/listevehicule.html",{"vehicules":vehicules})  
