from django.db import models

# Create your models here.

class Client(class (models.Model):

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name
