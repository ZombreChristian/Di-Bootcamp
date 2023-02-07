from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class InfoHotel(models.Model):
    emplacement = models.CharField(max_length=100)
    images = models.ImageField(upload_to= "images")
    description = models.TextField()
    
class Chambre(models.Model):
    number = models.IntegerField()
    
    def __str__(self) :
        return str(self.id)
    
    
    
class Reservation(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    heure = models.TimeField()  
    number_chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField() 
    nombre_jour = models.IntegerField()
    
    def __str__(self) :
        return str(self.nom,self.prenom)
    
class Commentaire(models.Model):
    hotel = models.ForeignKey(InfoHotel,null=True, on_delete= models.CASCADE, related_name='comments')
    nom_comm = models.CharField(max_length=100 , blank=True)
    auteur = models.ForeignKey(User, on_delete= models.CASCADE)
    corps = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.nom_comm = slugify("Commenté par " + str(self.auteur) + " a" + str(self.date_added))
        super.save(*args, **kwargs)
    def __str__(self):
        return self.nom_comm
    class Meta:
        ordering = ['-date_added']
        
        
class Personnel(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    number = models.IntegerField()
    email = models.EmailField(max_length=254)
    patron = 'Patron'
    receptionniste = 'Receptionniste'
    employe = 'Employé'
    
    type_user = [
        (patron,'patron'),(receptionniste,'receptionniste'),(employe,'employe')
    ]
    
    type_profile = models.CharField(max_length=100,choices= type_user,default=patron)
     
    def __str__(self):
        return self.user.username
    
class Reponse(models.Model):
    nom_comm = models.ForeignKey(Commentaire, on_delete= models.CASCADE, related_name= 'reponses')
    corps = models.TextField(max_length=500) 
    auteur = models.ForeignKey(User, on_delete= models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return "Reponse a" + str(self.nom_comm.nom_comm) 
    


         