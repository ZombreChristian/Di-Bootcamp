from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    
    
    

class VehiculeType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class TailleVehicule(models.Model)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
class Vehicule(models.Model):
    vehicule_type = models.ForeignKey(VehiculeType, verbose_name=("Type"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=False)
    prix = models.FloatField()
    taille = models.ForeignKey(TailleVehicule, verbose_name=("Taille"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vehicule_type
    