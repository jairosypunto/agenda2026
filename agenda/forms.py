from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria']  # Asegúrate de incluir los campos que deseas en el formulario  