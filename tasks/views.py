from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import reverse, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Category
from .forms import TaskModelForm, CategoryModelForm


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

    def catList(self):
        cat = Category.objects.all
        return cat

    def get_context_data(self, *args, **kwargs):
        context = super(TaskInsertView, self).get_context_data(*args, **kwargs)
        context['cat'] = self.catList()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TaskInsertView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("tasks.list")


class ListTasksView(LoginRequiredMixin, ListView):
    template_name = "tasks/task_lists.html"
    model = Task
    context_object_name = "tasks"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        """caso queira adicionar mais objetos no contexto"""
        context = super(ListTasksView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        search_task = self.request.GET.get("searchTask", "")
        user_logged = self.request.user
        query = Task.objects.filter(user=user_logged)
        if search_task:
            query = query.filter(title__contains=search_task) | query.filter(
                description__contains=search_task
            )
        return query.order_by("-id").all()

    def Done_Task(request, task_id):
        item = Task.objects.get(pk=task_id)
        item.done = not item.done
        item.save()
        messages.success(request, ("Task Atualizado!"))
        return HttpResponseRedirect("/tasks/")


class CategoryInsertView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryModelForm
    context_object_name = "category"
    template_name = "tasks/category_create.html"
    success_message = "Category created successfully!!!!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("tasks.insert")
