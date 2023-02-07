# login/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from account.models import Customer,RoomManager

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
    
    
    
class RegisterCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'role', 'profile_photo')