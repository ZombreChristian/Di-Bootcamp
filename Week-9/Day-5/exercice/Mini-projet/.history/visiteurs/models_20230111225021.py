from django.db import models

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    id = models.IntegerField()
    date_reservation = models.DateTimeField() 
    date_expira   