from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.TextField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name','last_name'] 
    
    
    

class TypeVehicule(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
    
class TailleVehicule(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
    
    
class Vehicule(models.Model):
    vehicule_type = models.ForeignKey(TypeVehicule, related_name=("Type"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    prix = models.FloatField()
    taille = models.ForeignKey(TailleVehicule, related_name=("Taille"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vehicule_type
    
    
class Location(models.Model):
    date_location = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(auto_now_add = True,null=True )
    client = models.ForeignKey(Client, related_name=("Client"), on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, related_name=("Vehicule"), on_delete=models.CASCADE)
    def __str__(self):
        return self.vehicule_type
    
    class Meta:
        ordering = ['date_location']
    
    
    
class TarifLocation(models.Model):
    tarif_jour = models.FloatField()
    type_vehicule = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    taille_vehicule = models.ForeignKey(TailleVehicule, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.type_vehicule 