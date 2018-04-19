from django.contrib import admin
from .models import Task, Event

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Event, TaskAdmin)
