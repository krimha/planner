from django.db import models

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    readonly_fields = ('created',)

    def __str__(self):
        return self.title
