from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:task_id>', views.toggle_task, name='toggle'),
    path('add', views.add_task, name='add'),
]
