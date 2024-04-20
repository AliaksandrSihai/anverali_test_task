from django.core.validators import RegexValidator
from django.db import models

from users.models import NULLABLE


# Create your models here.
class PerformerModel(models.Model):
    """ Модель для  исполнителя"""
    number_validator = RegexValidator(
        regex=r"^\+\d{9,15}$",
        message='Номер телефона должен начинаться с символа ' + ' и содержать 9-15 цифр',
    )

    name = models.CharField(max_length=255, verbose_name='имя')
    surname = models.CharField(max_length=255, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(
        max_length=15, verbose_name="номер телефона", unique=True, validators=[number_validator], **NULLABLE
    )
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    experience = models.PositiveIntegerField(verbose_name='опыт в годах', **NULLABLE)

    def __str__(self):
        return f"{self.name} -- {self.email}"

    class Meta:
        verbose_name = "исполнитель"
        verbose_name_plural = "исполнители"