from django.db import models

# Create your models here.

class Animal(models.Model):
    id = models.IntegerField()
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    fami = models.CharField(max_length= 20 , null= True)
    
    def __str__(self):
        return (self.id)
 
class Family(models.Model):
    id = models.IntegerField()
    nom = models.CharField(max_length= 20 , null= True)    
    
    def __str__(self):
        return (self.id)
    