from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    vidas = models.IntegerField(default=3)
    estado = models.CharField(max_length=20, choices=[
        ('normal', 'Normal'),
        ('dañado', 'Dañado'),
        ('gameover', 'Game Over')
    ], default='normal')

class Mision(models.Model):
    descripcion = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='misiones')
    tiempo_limite = models.DateTimeField()
    completada = models.BooleanField(default=False)

    def tiempo_restante(self):
        return self.tiempo_limite - now()
