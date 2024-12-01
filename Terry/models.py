from django.db import models
from Register.models import Usuarios  

class UserProfile(models.Model):
    user = models.OneToOneField(Usuarios, on_delete=models.CASCADE, related_name='terry_profile')
    trivias_completed = models.PositiveIntegerField(default=0)                                  # Número de trivias completadas
    lives = models.PositiveIntegerField(default=3)                                              # Número de vidas restantes
    active_skin = models.CharField(max_length=100, default="TerryNice.gif")                         # Nombre de la skin activa

    def __str__(self):
        return f"{self.user.email} - Trivias: {self.trivias_completed}, Vidas: {self.lives}, Skin: {self.active_skin}"
