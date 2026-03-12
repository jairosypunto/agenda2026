import os
import django
from datetime import timedelta

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from django.utils import timezone
from agenda.models import Task
from agenda.utils import enviar_telegram

def revisar_tareas():
    # Usamos timezone.now() para obtener la hora actual exacta
    ahora = timezone.now()
    
    # Filtramos tareas no completadas y que aún no han sido notificadas
    # Solo tomamos las que tienen una fecha de recordatorio establecida
    tareas_pendientes = Task.objects.filter(
        is_completed=False, 
        notificacion_enviada=False,
        reminder_time__isnull=False
    )
    
    for task in tareas_pendientes:
        # Calculamos el momento exacto del aviso: (Hora vencimiento) - (Minutos de antelación)
        # Usamos task.minutes_before definido en tu modelo
        momento_aviso = task.reminder_time - timedelta(minutes=task.minutes_before)
        
        # Si ya es el momento de avisar o ya pasó la hora de aviso:
        if ahora >= momento_aviso:
            mensaje = (
                f"⏰ Recordatorio: La tarea '{task.title}' vence pronto.\n"
                f"⏳ Antelación configurada: {task.minutes_before} minutos.\n"
                f"📝 Descripción: {task.description}"
            )
            
            # Enviar usando tu función de utils.py
            enviar_telegram(mensaje, task.user)
            
            # MARCAMOS COMO ENVIADA para no repetir el mensaje
            task.notificacion_enviada = True
            task.save()
            
            print(f"Notificación enviada para: {task.title}")

if __name__ == "__main__":
    revisar_tareas()