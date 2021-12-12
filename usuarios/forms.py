from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        """
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Insira seu nome de usuario...",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input",
                    "placeholder": "Insira seu email...",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "input",
                    "placeholder": "Insira sua senha...",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "input",
                    "placeholder": "Confirme sua senha...",
                }
            ),
        }
        """
