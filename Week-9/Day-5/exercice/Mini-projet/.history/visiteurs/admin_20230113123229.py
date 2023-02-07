from django.contrib import admin
from visiteurs.models import Chambre,InfoHotel,Reservation

# Register your models here.

admin.site.register(Chambre,InfoHotel,)
