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
        return str(self.number)

class Reservation(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    heure = models.TimeField()  
    number_chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField() 
    nombre_jour = models.IntegerField()
    
    def __str__(self) :
        return str(self.nom,self.prenom)
    




         