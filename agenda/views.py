from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from .utils import enviar_telegram
from .models import Task
from .forms import TaskForm



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'agenda/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(user=request.user, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                task = form.save(commit=False)
                task.user = request.user 
                task.save()
            
            # --- ACTIVAMOS EL BOT DINÁMICAMENTE ---
            if task.priority == 'H':
                # Construimos el mensaje con título y descripción
                mensaje = f"🔔 Tarea Urgente: {task.title}\n📝 Descripción: {task.description}"
                enviar_telegram(mensaje, request.user)
                
            messages.success(request, '¡Tarea creada con éxito!')
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'agenda/task_form.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(user=request.user, data=request.POST, instance=task)
        if form.is_valid():
            with transaction.atomic():
                task = form.save() 
            
            # --- AVISAR TAMBIÉN AL EDITAR SI ES URGENTE ---
            if task.priority == 'H':
                # Construimos el mensaje con título y descripción
                mensaje = f"🔔 Tarea Urgente (Actualizada): {task.title}\n📝 Descripción: {task.description}"
                enviar_telegram(mensaje, request.user)
            
            messages.success(request, 'Tarea actualizada correctamente.')
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user, instance=task)
    return render(request, 'agenda/task_form.html', {'form': form})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.info(request, 'Tarea eliminada.')
    return redirect('task_list')