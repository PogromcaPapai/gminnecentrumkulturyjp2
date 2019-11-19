from django import forms

from .models import User

class Register(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=20)
    password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

class Reserve(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=20)
    password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)