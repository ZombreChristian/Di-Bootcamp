from django.contrib import admin
from .models import Locataire


# Register your models here.

class LocataireAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'prenom', 'email', 'phone_number')
    search_fields = ['nom', 'prenom', 'phone_number', 'email']
    list_filter = ['nom', 'prenom', 'phone_number']
    list_per_page = 4
    
admin.site.register(Locataire,LocataireAdmin)    
