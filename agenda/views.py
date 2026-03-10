from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm  # <--- Importamos el formulario que creamos

# ESTA ES TU VISTA ORIGINAL (No la cambies)
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'agenda/lista_tareas.html', {'tareas': tareas})

# ESTA ES LA VISTA NUEVA (Se añade debajo)
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas') # Redirige a la lista después de guardar
    else:
        form = TareaForm()
    return render(request, 'agenda/crear_tarea.html', {'form': form})

def completar_tarea(request, tarea_id):
    # Buscamos la tarea por su ID único
    tarea = get_object_or_404(Tarea, id=tarea_id)
    # Cambiamos el estado
    tarea.completada = True
    tarea.save()
    # Regresamos a la lista
    return redirect('lista_tareas')

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        # Pasamos 'instance=tarea' para que guarde cambios en la misma fila
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        # Aquí cargamos los datos viejos en el formulario
        form = TareaForm(instance=tarea)
    
    return render(request, 'agenda/crear_tarea.html', {'form': form})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete() # ¡Esto borra la fila de la base de datos para siempre!
    return redirect('lista_tareas')