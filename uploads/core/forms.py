from django import forms

from .models import User

class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email")

class Reserve(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=20)
    password = forms.CharField(label='Hasło', max_length=100)