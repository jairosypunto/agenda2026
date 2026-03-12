import os
import django
import requests
from datetime import datetime, timedelta

# Configurar el entorno de Django para poder usar modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from agenda.models import Task

def revisar_tareas():
    ahora = datetime.now()
    # Buscamos tareas que faltan 30 min para su vencimiento
    # (ajusta el tiempo según tu campo de fecha en el modelo)
    limite = ahora + timedelta(minutes=30)
    
    # Filtramos tareas no completadas que vencen pronto
    tareas_urgentes = Task.objects.filter(reminder_time__lte=limite, is_completed=False)
    
    for task in tareas_urgentes:
        mensaje = f"⏰ Recordatorio: La tarea '{task.title}' vence en menos de 30 minutos."
        # Aquí reutilizas tu función, pero necesitas importar enviar_telegram
        # Tip: Podrías mover enviar_telegram a un archivo 'utils.py'
        print(f"Notificando: {task.title}")

if __name__ == "__main__":
    revisar_tareas()