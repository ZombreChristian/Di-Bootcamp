from django.contrib import admin

# Register your models here.

class LocataireAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'prenom', 'email', 'phone_number', 'loue', 'date_location')
    search_fields = ['nom', 'prenom', 'phone_number', 'email']
    list_filter = ['nom', 'prenom', 'phone_number']
    list_per_page = 4
