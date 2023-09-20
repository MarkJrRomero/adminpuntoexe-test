from django.contrib.auth.models import AbstractUser
from django.db import models
from auditlog.registry import auditlog

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=300, null=False)
    nombres = models.CharField(max_length=300)
    telefono = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cedula = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Usuario"
        db_table = 'user_usuarios'

    def __str__(self):
        return str(self.username) + ' ' + str(self.cedula)

auditlog.register(CustomUser)
