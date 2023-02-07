from django.db import models

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    id = models.IntegerField()
    heure = models.TimeField()
    date_reservation = models.DateTimeField() 
    date_expiration =  models.DateTimeField()
    
class Reservation(class (models.Model):

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)       