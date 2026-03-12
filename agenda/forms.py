from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'reminder_time', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la tarea...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'reminder_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local' 
            }),
        }

    def __init__(self, *args, **kwargs):
        # Extraemos 'user' de los kwargs. Si no existe, será None.
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtramos solo si el usuario fue provisto. 
        # Esto hace que el formulario sea más flexible y no falle en contextos de depuración.
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)