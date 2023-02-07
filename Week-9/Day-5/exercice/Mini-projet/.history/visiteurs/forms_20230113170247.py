from django import forms
from visiteurs.models import Reservation

class LocataireForm(forms.ModelForm):
    
    class Meta:
        model = Locataire
        fields = '__all__'
        