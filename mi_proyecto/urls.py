from django.contrib import admin
from django.urls import path, include # <--- ¡Mastica esto! Necesitamos 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')), # <--- ¡Este es el puente!
]