from django.db import models

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    id = models.IntegerField()
    
    def __str__(self) :
        return str(self.id)
    
    
    
class Reservation(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    heure = models.TimeField()  
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField() 
    date_expiration =  models.DateTimeField()
    
    def __str__(self) :
        return str(self.nom,self.prenom)
    
    
         