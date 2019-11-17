from django import forms
import models

class Register(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "password", "email")

class Reserve(forms.Form):
    seat = forms.IntegerField(widget=forms.HiddenInput())
    event = forms.CharField(max_length=100, widget=forms.HiddenInput())
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100)