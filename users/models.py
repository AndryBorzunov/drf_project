from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

METHOD_PAY_CHOICES = [("cash", "Наличные"), ("transfer", "Перевод на счет")]


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="E-mail", help_text="Укажите E-mail"
    )

    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name="Город проживания",
        help_text="Укажите родной город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="payments",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оплаты", help_text="Укажите дату оплаты"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный курс",
        help_text="Выберите учебный курс",
        related_name="courses",
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный урок",
        help_text="Выберите урок",
        related_name="lessons",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        help_text="Введите сумму оплаты",
    )

    method_pay = models.CharField(
        max_length=16,
        choices=METHOD_PAY_CHOICES,
        default="transfer",
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        ordering = ["-created_at"]
        unique_together = ["user", "course", "lesson"]
        indexes = [models.Index(fields=["user", "course", "lesson"])]
