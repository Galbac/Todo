from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    CreateView,
    DeleteView,
)

from .models import TodoList
from .forms import TodoForm


# Create your views here.


class TodoListView(ListView):
    model = TodoList
    paginate_by = 6
    template_name = "todo/todo_list.html"
    context_object_name = "todos"


class ToDoUpdate(UpdateView):
    template_name = "todo/todo_update.html"
    slug_url_kwarg = "slug"
    model = TodoList
    form_class = TodoForm
    success_url = reverse_lazy("home")


class ToDoDetailView(DetailView):
    template_name = "todo/todo_detail.html"
    model = TodoList
    context_object_name = "todo"


class ToDoCreateView(CreateView):
    template_name = "todo/todo_update.html"
    model = TodoList
    form_class = TodoForm
    context_object_name = "todo"
    success_url = reverse_lazy("home")


class ToDoDelete(DeleteView):
    model = TodoList
    success_url = reverse_lazy("home")
    template_name = "todo/todo_delete.html"
    context_object_name = "todo"
