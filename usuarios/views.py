from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastrar.html"
    form_class = UsuarioForm
