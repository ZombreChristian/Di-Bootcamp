from django import forms
from rent.models import C

class LocataireForm(forms.ModelForm):
    
    class Meta:
        model = Locataire
        fields = '__all__'
        