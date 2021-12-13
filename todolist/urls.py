from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include


urlpatterns = [
    # path("", RedirectView.as_view(url="/tasks")),
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("tasks/", include("tasks.urls")),
    path("usuarios/", include("usuarios.urls")),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
