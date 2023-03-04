from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'isImportant']
        #for styling in the app we can use widgets
        #widgets = {
        #    'title': forms.TextInput(attrs={'class': 'form-control'})
        #}

