from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Profile(AbstractUser):
    first_name = models.CharField(max_length=40, blank=True, verbose_name="Имя", default="default")
    last_name = models.CharField(max_length=40, blank=True, verbose_name="Фамилия", default="default")
    patronymic = models.CharField(max_length=40, blank=True, verbose_name="Отчество", default="default")
    phone_number = PhoneNumberField(null=True, blank=True, unique=True, verbose_name="Номер телефона")
    email = models.EmailField(blank=True)
    is_designer = models.BooleanField(default=False, verbose_name="Дизайнер")
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"