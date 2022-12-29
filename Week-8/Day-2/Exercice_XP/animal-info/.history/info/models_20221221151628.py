from django.db import models

# Create your models here.

class Animal(models.Model):
    id = models.IntegerField()
    pattes = models.IntegerField()
    poids = models.IntegerField()
    hauteur = models.IntegerField()
    vitesse = models.IntegerField()
    famille = models.CharField(max_length= 20 , null= True)
    
    def __str__(self):
        return (self.id)
 
class Family(models.Model):
    id = models.IntegerField()
    nom = models.CharField(max_length= 20 , null= True)    
    
    def __str__(self):
        return (self.id)
    