from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, mail, contraseña=None, **extra_fields):
        if not mail:
            raise ValueError('El correo electrónico es obligatorio.')
        mail = self.normalize_email(mail)
        user = self.model(nombre=nombre, mail=mail, **extra_fields)
        user.set_password(contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, mail, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nombre, mail, contraseña, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    nombre     = models.CharField(max_length=25, unique=True)
    mail       = models.EmailField(unique=True)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre
