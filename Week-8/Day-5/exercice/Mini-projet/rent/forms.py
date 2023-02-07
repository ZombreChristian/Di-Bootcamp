from django import forms
from rent.models import Client, Vehicule, TypeVehicule, TailleVehicule , Location , TarifLocation


class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
class VehiculeForm(forms.ModelForm):
    
    class Meta:
        model = Vehicule
        fields = '__all__'
        
        
class LocationForm(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = '__all__'
                
                