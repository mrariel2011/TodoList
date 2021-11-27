from django import forms
from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_to",
        ]
        """
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add some title here",
                }
            ),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_to": forms.TextInput(attrs={"class": "form-control"}),
        }
        """
