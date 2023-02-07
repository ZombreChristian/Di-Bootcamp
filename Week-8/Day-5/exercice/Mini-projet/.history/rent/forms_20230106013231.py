from django import forms
from rent.models import Client

class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Locataire
        fields = '__all__'
        