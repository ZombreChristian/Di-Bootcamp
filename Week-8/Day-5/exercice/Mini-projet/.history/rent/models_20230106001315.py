from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(_(""), max_length=50)

    

    
    def __str__(self):
        return self.name