from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    #Para elegir que campo será utilizado para iniciar sesión
    USERNAME_FIELD = 'email'
    #Campos requeridos al crear un nuevo usuario
    REQUIRED_FIELDS = []