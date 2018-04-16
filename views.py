from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm

def tasks(request):
    tasks = Task.objects.all()
    task_form = TaskForm()

    context = {
        'tasks': tasks,
        'form': task_form,
    }
    return render(request, 'planner/tasks.html', context)

def task_details(request, task_id):

    return render(request, 'planner/details.html')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done ^= True
    task.save()
    return redirect('tasks')

@require_POST
def add_task(request):

    form = TaskForm(request.POST)

    if form.is_valid():
        task = Task(title=request.POST['task_title'])
        task.save()

    return redirect('tasks')

