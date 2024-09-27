from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    FACILITATOR = 'FACILITATOR', 'Facilitador'
    DIRECTOR = 'DIRECTOR', 'Directivo'
    PARTNER = 'PARTNER', 'Socio'

class RoleType(models.TextChoices):
    PRESIDENT = 'PRESIDENTE', 'Presidente'
    SECRETARIO = 'SECRETARIO', 'Secretario'
    TESORERO = 'TESORERO', 'Tesorero'
    VOCAL = 'VOCAL', 'Vocal'
    SOCIO = 'SOCIO', 'Socio'
    NONE = 'NONE', 'None'
    
class CustomUser(AbstractUser):
    document_type = models.CharField(max_length=3, choices=[('DNI', 'DNI'), ('CE', 'CE')])
    full_name = models.CharField(max_length=255, null=False)
    document_number = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    shares = models.IntegerField(default=0)
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.PARTNER)
    role_type =models.CharField(max_length=20, choices=RoleType.choices,default=RoleType.NONE)

    