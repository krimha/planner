from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle', views.toggle_task, name='toggle'),
    path('add', views.add_task, name='add'),
]
