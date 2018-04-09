from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    task_form = TaskForm()

    context = {
        'tasks': tasks,
        'form': task_form,
    }
    return render(request, 'planner/index.html', context)

@require_POST
def toggle_task(request):
    # TODO: Should this be done using a form, and more safely
    if request.is_ajax():
        task_id = request.POST['task_id']
        task = get_object_or_404(Task, pk=task_id)
        task.done ^= True
        task.save()

    return render(request, 'planner/task.html', {'task': task})

@require_POST
def add_task(request):

    form = TaskForm(request.POST)

    if form.is_valid():
        task = Task(title=request.POST['task_title'])
        task.save()

    return redirect('index')

