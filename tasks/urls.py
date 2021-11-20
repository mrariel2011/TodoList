from django.urls import path
from django.urls.conf import include
from django.views.generic.base import View

from tasks.models import Task
from .views import ListTasksView


urlpatterns = [
    path("", ListTasksView.as_view(), name="tasks.list"),
    path("addTask/", ListTasksView.Add_Task),
    path("deleteTask/<task_id>", ListTasksView.Delete_Task, name="deleteTask"),
    path("doneTask/<task_id>", ListTasksView.Done_Task, name="doneTask"),
    path("editTask/<task_id>", ListTasksView.Edit_Task, name="editTask"),
]
