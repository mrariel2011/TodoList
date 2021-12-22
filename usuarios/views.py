from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastrar.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("homepage.home")
