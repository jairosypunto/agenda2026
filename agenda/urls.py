from django.urls import path
from . import views

urlpatterns = [
    # Ahora la ruta raíz llama a 'task_list'
    path('', views.task_list, name='task_list'),
    
    # Rutas para crear, editar, eliminar y completar
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]