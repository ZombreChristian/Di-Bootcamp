from django.contrib import admin
f

# Register your models here.

class LocataireAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'prenom', 'email', 'phone_number')
    search_fields = ['nom', 'prenom', 'phone_number', 'email']
    list_filter = ['nom', 'prenom', 'phone_number']
    list_per_page = 4
    
admin.site.register(Admin)    
