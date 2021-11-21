from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
from django.http.response import JsonResponse


class ListTasksView(TemplateView):
    template_name = "tasks/lists.html"

    def get_context_data(self, **kwargs):
        context = super(ListTasksView, self).get_context_data(**kwargs)
        context["tasks"] = Task.objects.order_by("-id")
        return context

    def Add_Task(request):
        new_item = Task(
            title=request.POST["title"],
            description=request.POST["description"],
            due_to=request.POST["due_to"],
        )
        new_item.save()
        messages.success(request, ("Task Adicionado!"))
        return HttpResponseRedirect("/tasks/")

    def Delete_Task(request, task_id):
        item = Task.objects.get(pk=task_id)
        item.delete()
        messages.success(request, ("Task deletado!"))
        return HttpResponseRedirect("/tasks/")

    def Done_Task(request, task_id):
        item = Task.objects.get(pk=task_id)
        item.done = not item.done
        item.save()
        messages.success(request, ("Task Atualizado!"))
        return HttpResponseRedirect("/tasks/")

    def Edit_Task(request, task_id):
        if request.method == "POST":
            item = Task.objects.get(pk=task_id)
            new_value = request.POST.get("title")
            item = Task(
                task_id,
                request.POST.get("title"),
                request.POST.get("description"),
                request.POST.get("due_to"),
            )
            item.save()
            messages.success(request, ("Task Editado!"))
            return HttpResponseRedirect("/tasks/")
        else:
            goItem = Task.objects.get(pk=task_id)
            return render(request, "tasks/edit.html", {"task": goItem})
