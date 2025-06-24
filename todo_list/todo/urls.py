from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import TodoListView, ToDoUpdate, ToDoDetailView, ToDoCreateView, ToDoDelete

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo-update/<slug:slug>/', ToDoUpdate.as_view(), name='todo_update'),
    path('todo-detail/<slug:slug>/', ToDoDetailView.as_view(), name='todo_detail'),
    path('todo-create/', ToDoCreateView.as_view(), name='todo_create'),
    path('todo-delete/<slug:slug>/', ToDoDelete.as_view(), name='todo_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)