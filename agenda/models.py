from django.db import models

class Tarea(models.Model):
    CATEGORIAS = [
        ('SOFTWARE', 'Desarrollo de Software'),
        ('INGLES', 'Aprendizaje de Inglés'),
        ('OTRO', 'Otras tareas'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTRO') # <--- Nuevo campo

    def __str__(self):
        return self.titulo