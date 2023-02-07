from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    number = models.IntegerField()
    
    def __str__(self) :
        return str(self.id)
    
class Personnel(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    number = models.IntegerField()
    email = models.EmailField(max_length=254)
    patron = 'Patron'
    receptionniste = 'Receptionniste'
    employe = 'Employé'
    
    type_user = [
        (patron,'patron'),(receptionniste,'receptionniste'),(employe,'employe')
    ]
    
    type_profile = models.CharField(max_length=100,choices= type_user,default=patron)
     
    def __str__(self):
        return self.nom    
    
class Reservation(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    heure = models.TimeField()  
    number_chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField() 
    nombre_jour = models.IntegerField()
    
    def __str__(self) :
        return str(self.nom,self.prenom)
    




         