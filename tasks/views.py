from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task


class ListTasksView(TemplateView):
    template_name = "tasks/lists.html"

    def get_context_data(self, **kwargs):
        context = super(ListTasksView, self).get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(done=False)
        return context

    def Add_Task(request):
        new_item = Task(
            title=request.POST["title"],
            description=request.POST["description"],
        )
        new_item.save()
        return HttpResponseRedirect("/tasks/")
