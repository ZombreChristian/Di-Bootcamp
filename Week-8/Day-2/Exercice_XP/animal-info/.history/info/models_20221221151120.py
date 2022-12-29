from django.db import models

# Create your models here.

class Animal(models.Model):
    id = models.IntegerField()
    pattes = models.IntegerField()
    poids = models.IntegerField()
    hauteur = models.IntegerField()
    vitesse = models
    