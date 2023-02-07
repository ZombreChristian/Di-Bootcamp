from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class LocataireAdmin():
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, verbose_name="Numero de téléphone", null=True)
    