from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category'] # 'is_completed' se suele manejar aparte
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }