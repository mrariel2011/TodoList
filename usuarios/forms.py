from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        """
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira seu nome de usuario...",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira seu email...",
                }
            ),
            "password": forms.Password(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira sua senha...",
                }
            ),
        }
        """
