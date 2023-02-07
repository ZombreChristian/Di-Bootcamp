from django import forms
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation


class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
class VehiculeForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
                