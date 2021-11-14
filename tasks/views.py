from django.views.generic import TemplateView

from .models import Task


class ListTasksView(TemplateView):
    template_name = "tasks/lists.html"

    def get_context_data(self, **kwargs):
        context = super(ListTasksView, self).get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(done=False)
        return context
