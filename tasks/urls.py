from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListTasksView.as_view(), name="tasks.list"),
    path("<int:page>/", views.ListTasksView.as_view(), name="tasks.list/"),
    path("insert", views.TaskInsertView.as_view(), name="tasks.insert"),
    path("update/<pk>", views.TaskUpdateView.as_view(), name="tasks.update"),
    path("delete/<pk>", views.TaskDeleteView.as_view(), name="tasks.delete"),
    path("doneTask/<task_id>", views.ListTasksView.Done_Task, name="doneTask"),
    path("category", views.CategoryInsertView.as_view(), name="tasks.category"),
]
