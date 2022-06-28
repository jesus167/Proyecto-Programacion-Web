from django.urls import path

from .views import registro_final



urlpatterns = [
    
    path('', registro_final, name="Registro"),
    
]
