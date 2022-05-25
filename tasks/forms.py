from django import forms
from .models import Task, Category


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_to",
            "category",
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


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        """
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add a name here",
                }
            )
        }
        """
