from django.db import models



class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField(blank=False, null=False)
    end = models.DateTimeField(default=None, blank=True, null=True)


    def __str__(self):
        return self.title




