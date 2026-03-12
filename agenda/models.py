from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """Modelo para extender la información del usuario."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telegram_id = models.CharField(max_length=50, blank=True, null=True, help_text="ID de Telegram para notificaciones.")

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Señal para crear el perfil automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories', db_index=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#007bff')
    
    class Meta:
        unique_together = ('user', 'name')
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
class Task(models.Model):
    PRIORITY_CHOICES = [('L', 'Low'), ('M', 'Medium'), ('H', 'High')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False, db_index=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reminder_time = models.DateTimeField(null=True, blank=True)
    
    # --- NUEVO: Tiempo de antelación personalizado (en minutos) ---
    minutes_before = models.PositiveIntegerField(default=15, help_text="¿Cuántos minutos antes quieres el aviso?")
    
    # El semáforo para el bot
    notificacion_enviada = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['user', 'is_completed', 'notificacion_enviada'])]

    def __str__(self):
        return self.title
    

    def time_left(self):
        if self.reminder_time and not self.is_completed:
            now = timezone.now()
            if self.reminder_time > now:
                diff = self.reminder_time - now
                days = diff.days
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                parts = [f"{days}d" if days > 0 else "", f"{hours}h" if hours > 0 else "", f"{minutes}m"]
                return f"{' '.join([p for p in parts if p])} remaining"
            return "Time expired!"
        return None
    
    