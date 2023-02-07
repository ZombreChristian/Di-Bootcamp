from django.db import models

# Create your models here.

class AdminModel()
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, verbose_name="Numero de téléphone", null=True)
    date_location = models.DateField(null=True) 