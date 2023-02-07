from django import forms
from visiteurs.models import Reservation

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Res
        fields = '__all__'
        