from django.contrib import admin
from .models import Tarea # 1. Importamos tu modelo 'Tarea'

# 2. Le decimos al administrador: "Por favor, muestra la tabla Tarea"
admin.site.register(Tarea)