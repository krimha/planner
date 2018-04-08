from django import forms

class TaskForm(forms.Form):
    task_title = forms.CharField(label='New Task', max_length=100)

