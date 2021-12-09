from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task
from .forms import TaskModelForm


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskModelForm
    context_object_name = "task"
    template_name = "tasks/task_update.html"
    success_message = "Task updated successfully!!!!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("tasks.list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    form_class = TaskModelForm
    context_object_name = "task"
    template_name = "tasks/task_delete.html"
    success_message = "Task deleted successfully!!!!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("tasks.list")


class TaskInsertView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskModelForm
    context_object_name = "task"
    template_name = "tasks/task_create.html"
    success_message = "Task created successfully!!!!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TaskInsertView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("tasks.list")


class ListTasksView(LoginRequiredMixin, TemplateView):
    template_name = "tasks/task_lists.html"

    def get_context_data(self, **kwargs):
        context = super(ListTasksView, self).get_context_data(**kwargs)
        context["tasks"] = []

        user_logged = self.request.user
        if user_logged.is_authenticated:
            context["tasks"] = Task.objects.filter(user=user_logged).order_by("-id")
        else:
            messages.warning(self.request, ("Entre para interagir!"))
        return context

    def Done_Task(request, task_id):
        item = Task.objects.get(pk=task_id)
        item.done = not item.done
        item.save()
        messages.success(request, ("Task Atualizado!"))
        return HttpResponseRedirect("/tasks/")
