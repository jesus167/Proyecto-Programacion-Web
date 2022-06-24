from django.db import models

# Create your models here.

class RegistrarUsuario(models.Model):

    nombre = models.CharField(max_length=50, blank= True)
    correo =  models.EmailField(max_length=100, blank= True)
    clave = models.CharField(max_length=50, blank= True)
    estado = models.BooleanField()