<<<<<<< HEAD
from django.urls import path

from .views import registro_final



urlpatterns = [
    
    path('', registro_final, name="Registro"),
    
]
=======
from django.urls import path

from . import views



urlpatterns = [
    
    path('', views.registro, name="Registro"),
    
]
>>>>>>> 128f23bed87f8a9a4e0bea8c474957b0d83c30c8
