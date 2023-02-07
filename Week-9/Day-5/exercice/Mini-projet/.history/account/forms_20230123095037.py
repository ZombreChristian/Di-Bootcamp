# login/forms.py
from django import forms
from django.contrib.auth import get_user_model

from account.models import Customer,RoomManager

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
    
    
    
class RegisterCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class RegisterRoomManagerForm(forms.ModelForm):
    class Meta:
        model = RoomManager
        fields = '__all__'        