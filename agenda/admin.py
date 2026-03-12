from django.contrib import admin
from .models import Category, Task, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram_id')
    search_fields = ('user__username', 'telegram_id')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'color')
    list_filter = ('user',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # 'list_editable' te permite cambiar el estado de completado directamente desde la lista
    list_display = ('title', 'user', 'category', 'priority', 'is_completed', 'reminder_time', 'created_at')
    list_editable = ('is_completed', 'priority') 
    
    # Filtros laterales avanzados
    list_filter = ('is_completed', 'priority', 'category', 'user', 'created_at')
    
    # Búsqueda optimizada (busca en campos relacionados con __username)
    search_fields = ('title', 'description', 'user__username')
    
    # Orden predeterminado
    ordering = ('-created_at',)
    
    # Agrupación de campos para editar una tarea de forma más organizada
    fieldsets = (
        ('Información Básica', {
            'fields': ('user', 'title', 'description', 'category', 'priority')
        }),
        ('Fechas y Estado', {
            'fields': ('is_completed', 'reminder_time')
        }),
    )