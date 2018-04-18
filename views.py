from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm

import datetime as dt

def tasks(request):
    tasks = Task.objects.all()
    task_form = TaskForm()

    context = {
        'tasks': tasks,
        'form': task_form,
    }
    return render(request, 'planner/tasks.html', context)

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    return render(request, 'planner/details.html', {'task': task})

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


def schedule(request, year=None, month=None, day=None, week=None):
    now = dt.datetime.now()
    current_year, current_week, current_weekday = now.isocalendar()

    if not year:
        year = current_year

    if not week:
        if month and day:
            # TODO Infer week number
            week = 1

        # We did not supply anything. Default to current week.
        else:
            # TODO: Might want to offset by one. Check start and end of year.
            week = current_week

    # get start and end date of week
    monday = dt.datetime.strptime('{}-{}-1'.format(year, week), "%Y-%W-%w")
    sunday = monday + dt.timedelta(days=6)



    context = {
        'year': year,
        'week': week,
        'monday': monday,
        'sunday': sunday,
    }
    return render(request, 'planner/schedule.html', context)

