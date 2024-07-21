from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", **NULLABLE
    )
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Страна", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"


class Payments(models.Model):
    method_choices = [
        ('CASH', 'Наличными'),
        ('TRANSFER', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Пользователь'),
    date_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты'),
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE),
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE),
    payment_sum = models.PositiveIntegerField(verbose_name='Cумма платежа')
    payment_method = models.CharField(max_length=50, choices=method_choices, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.user} - {self.paid_course if self.paid_course else self.paid_lesson}'
