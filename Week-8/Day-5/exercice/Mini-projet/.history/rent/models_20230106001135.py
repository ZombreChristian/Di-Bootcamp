from django.db import models

# Create your models here.

class Client (models.Model):

    

    class Meta:
        
    def __str__(self):
        return self.name