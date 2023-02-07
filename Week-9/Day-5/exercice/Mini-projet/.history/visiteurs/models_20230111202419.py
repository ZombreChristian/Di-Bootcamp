from django.db import models

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(_(""), max_length=50)