from django.urls import path
from .views import TaskView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_view'),
    path('edit_task/<int:task_id>/', TaskView.as_view(), name='edit_task')
]
