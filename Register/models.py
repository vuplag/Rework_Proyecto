from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre     = models.CharField(max_length = 25)
    contraseña = models.CharField(max_length = 20)
    mail       = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
