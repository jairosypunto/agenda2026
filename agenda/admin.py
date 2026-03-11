from django.contrib import admin
from .models import Category, Task # 1. Importamos los dos nuevos modelos

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_completed', 'created_at')
    list_filter = ('category', 'is_completed') # Filtros profesionales en el admin
    search_fields = ('title',)