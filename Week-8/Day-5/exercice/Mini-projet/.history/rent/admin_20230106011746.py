from django.contrib import admin
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation

admin.site.register(Client)
admin.site.register(Vehicule)
admin.site.register(TypeVehicule)
admin.site.register(TailleVehicule)
admin.site.register(Location)
admin.site.register(TarifLocation)