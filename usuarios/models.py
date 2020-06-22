from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Usuario(AbstractUser):

    email = models.EmailField(unique=True)
    celular = PhoneNumberField()
    foto = models.ImageField(upload_to='usuario', blank=True, null=True)
    descripcion = models.TextField(max_length=1000, blank=True, null=True)