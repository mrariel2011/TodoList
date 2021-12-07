from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="usuarios.login",
    ),
    path("cadastrar/", views.UsuarioCreate.as_view(), name="usuarios.cadastrar"),
]
