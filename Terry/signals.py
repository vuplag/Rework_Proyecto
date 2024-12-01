from django.db.models.signals import post_save
from django.dispatch import receiver
from Register.models import Usuarios  # Importa tu modelo de usuario
from .models import UserProfile  # Importa el modelo de perfil

@receiver(post_save, sender=Usuarios)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
