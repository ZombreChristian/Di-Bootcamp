from django import forms
from visiteurs.models import Reservation

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reserca
        fields = '__all__'
        