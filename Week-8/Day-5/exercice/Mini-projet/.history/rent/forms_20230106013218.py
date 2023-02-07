from django import forms
from rent.models import Client

class LocatForm(forms.ModelForm):
    
    class Meta:
        model = Locataire
        fields = '__all__'
        