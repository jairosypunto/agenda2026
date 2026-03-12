import os
import django
# Importamos la función que moviste a utils.py
from agenda.utils import enviar_telegram

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from django.utils import timezone
from agenda.models import Task

def revisar_tareas():
    # Usamos timezone.now() para ser consistentes con la base de datos
    ahora = timezone.now()
    limite = ahora + timezone.timedelta(minutes=30)
    
    # Filtramos: que venza pronto, no completada y que NO se haya avisado ya
    tareas_pendientes = Task.objects.filter(
        reminder_time__lte=limite, 
        is_completed=False, 
        notificacion_enviada=False
    )
    
    for task in tareas_pendientes:
        mensaje = f"⏰ Recordatorio: La tarea '{task.title}' vence en menos de 30 minutos.\n📝 Descripción: {task.description}"
        
        # Enviar usando tu función de utils.py (necesita el usuario asociado a la tarea)
        enviar_telegram(mensaje, task.user)
        
        # MARCAMOS COMO ENVIADA para no repetir el mensaje
        task.notificacion_enviada = True
        task.save()
        
        print(f"Notificación enviada para: {task.title}")

if __name__ == "__main__":
    revisar_tareas()