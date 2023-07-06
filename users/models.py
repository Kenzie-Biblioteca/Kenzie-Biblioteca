from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=128)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)