from django.urls import path
from django.urls.conf import include
from django.views.generic.base import View

from tasks.models import Task
from .views import ListTasksView


urlpatterns = [
    path("", ListTasksView.as_view(), name="tasks.list"),
    path("addTask/", ListTasksView.Add_Task),
]
