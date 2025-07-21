from django import forms

from .models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["photo", "title", "description", "is_completed", "due_date"]
        widgets = {
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }
