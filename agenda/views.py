from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Importamos el modelo en inglés
from .forms import TaskForm  # Importamos el formulario en inglés

def task_list(request):
    # 'all()' trae todos los registros. Ordenamos por fecha de creación descendente
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'agenda/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'agenda/task_form.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'agenda/task_form.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')