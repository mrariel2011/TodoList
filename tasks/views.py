from django.views.generic import TemplateView


class ListTasksView(TemplateView):
    template_name = "tasks/lists.html"

    def get_context_data(self, **kwargs):
        context = super(ListTasksView, self).get_context_data(**kwargs)
        context['tasks'] = [
            {
                "id": 1,
                "title": "Task 1",
            },
            {
                "id": 2,
                "title": "Task 2",
            },
            {
                "id": 3,
                "title": "Task 3",
                "done": True
            }
        ]
        return context