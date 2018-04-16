from django.urls import path

from . import views

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('details/<int:task_id>', views.task_details, name='details'),
    path('complete/<int:task_id>', views.toggle_task, name='toggle'),
    path('add', views.add_task, name='add'),
]
