from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель для пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=135, verbose_name="город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
