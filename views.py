from django.shortcuts import get_object_or_404, render

from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'planner/index.html', {'tasks': tasks})


