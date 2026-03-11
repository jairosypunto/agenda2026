from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff')  # Color in hex format
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title