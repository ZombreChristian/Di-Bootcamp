from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    

    
    def __str__(self):
        return self.name