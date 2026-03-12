from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # Agregamos 'minutes_before' a la lista de campos
        fields = ['title', 'description', 'category', 'reminder_time', 'minutes_before', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border-primary', # Estilo azul
                'placeholder': 'Título de la tarea...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control border-primary', 
                'rows': 3
            }),
            'category': forms.Select(attrs={'class': 'form-select border-primary'}),
            'priority': forms.Select(attrs={'class': 'form-select border-primary'}),
            'reminder_time': forms.DateTimeInput(attrs={
                'class': 'form-control border-primary',
                'type': 'datetime-local' 
            }),
            'minutes_before': forms.NumberInput(attrs={
                'class': 'form-control border-primary',
                'min': 0,
                'placeholder': 'Minutos antes...'
            }),
        }
        labels = {
            'minutes_before': 'Antelación del aviso (minutos)',
        }
        help_texts = {
            'minutes_before': 'Ej: 15 para 15 minutos antes, 60 para 1 hora antes.',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)