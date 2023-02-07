from django.db import models

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    id = models.IntegerField()
    heure = models.TimeField()
    date_reservation = models.DateTimeField() 
    date_expiration =  models.DateTimeField()
    
class Reservation(models.Model):
    nom = models.CharField(_"), max_length=50)       