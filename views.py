from django.shortcuts import get_object_or_404, render, redirect

from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'planner/index.html', {'tasks': tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done ^= True
    task.save()
    return redirect('index')


