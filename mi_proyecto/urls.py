from django.contrib import admin
from django.urls import path, include # <--- ¡Mastica esto! Necesitamos 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')), # <--- Para manejar autenticación
    path('', include('agenda.urls')), # <--- ¡Este es el puente!
]