from django.db import models

from django import Faker

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    address = models.TextField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name)
    
    
    
    

class TypeVehicule(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
    
class TailleVehicule(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
    
    
class Vehicule(models.Model):
    vehicule_type = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    prix = models.FloatField()
    taille = models.ForeignKey(TailleVehicule,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.vehicule_type)
    
    
class Location(models.Model):
    date_location = models.DateTimeField()
    date_retour = models.DateTimeField(null=True )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date_location)
    
    
    
    
class TarifLocation(models.Model):
    tarif_jour = models.FloatField()
    type_vehicule = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    taille_vehicule = models.ForeignKey(TailleVehicule, on_delete=models.CASCADE) 
    
    def __str__(self):
        return str(self.type_vehicule )
    
    
class Faker():
    fake = Faker()
    for x in range(30):
            nom=fake.first_name(),
            prenom=fake.last_name(),
            email=fake.email(),
            phonenumber=fake.phone_number(),
            adresse=fake.address(),
            ville=fake.city(),
            pays=fake.country()   