from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include

urlpatterns = [
    path('', RedirectView.as_view(url='/tasks')),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
