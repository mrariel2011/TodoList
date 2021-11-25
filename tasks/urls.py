from django.urls import path


from . import views


urlpatterns = [
    path("", views.ListTasksView.as_view(), name="tasks.list"),
    path("update/<pk>", views.TaskUpdateView.as_view(), name="tasks.update"),
    # Apagar
    path("addTask/", views.ListTasksView.Add_Task),
    path("deleteTask/<task_id>", views.ListTasksView.Delete_Task, name="deleteTask"),
    path("doneTask/<task_id>", views.ListTasksView.Done_Task, name="doneTask"),
    path("editTask/<task_id>", views.ListTasksView.Edit_Task, name="editTask"),
]
