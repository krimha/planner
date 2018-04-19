from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.db.models.functions import TruncDate
from django.db.models import Count

from .models import Task, Event
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


def handle_date_string(date_string):
    '''Handles the date string for the schedule view.

    Parameters:
    date_string: A string representing either a week in a year, where the week
        number is prepended with "W", or a specific date.

    Returns:
    A dictionary containing the year and week number as ints, and the monday
    and sunday of that week as datetime objects.
    '''

    if not date_string:
        return handle_date_string(dt.datetime.now().strftime('%Y-%m-%d'))

    day = None
    try:
        day = dt.datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        pass

    try:
        day = dt.datetime.strptime(date_string + '-1', '%Y-W%W-%w')
    except ValueError:
        pass

    if not day:
        return handle_date_string(dt.datetime.now().strftime('%Y-W%W'))

    year, week, weekday = day.isocalendar()

    monday = day - dt.timedelta(days=weekday-1)
    sunday = monday + dt.timedelta(days=6)

    context = {
        'monday': monday,
        'sunday': sunday,
        'week': week,
        'year': year,
        'previous_string': (monday - dt.timedelta(days=7)).strftime('%Y-W%W'),
        'next_string': (monday + dt.timedelta(days=7)).strftime('%Y-W%W'),
    }

    return context



def schedule(request, date_string=None):

    context = handle_date_string(date_string)

    WEEKDAYS = ['monday', 'tueday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday']
    week_start = context['monday']
    week_end   = context['sunday'] + dt.timedelta(hours=23, minutes=59, seconds=59)

    week_events = Event.objects.filter(start__range=[week_start, week_end])

    events_by_day = {}

    for i, weekday in enumerate(WEEKDAYS):
        day_start = week_start+dt.timedelta(days=i)
        day_delta = dt.timedelta(hours=23, minutes=59, seconds=59)
        events_by_day[weekday] = week_events.filter(start__range=[day_start,
                                                                  day_start+day_delta])

    context['week_events'] = events_by_day

    return render(request, 'planner/schedule.html', context)

