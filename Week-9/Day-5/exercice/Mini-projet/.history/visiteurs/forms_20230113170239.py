from django import forms
from vente.models import Reservation

class LocataireForm(forms.ModelForm):
    
    class Meta:
        model = Locataire
        fields = '__all__'
        