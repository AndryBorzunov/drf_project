from django.db import models
from embed_video.fields import EmbedVideoField


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )

    preview = models.ImageField(
        upload_to="lms/previews/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите превью курса",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Укажите учебный курс",
        blank=True,
        null=True,
        related_name="lessons",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )

    preview = models.ImageField(
        upload_to="lms/previews/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите превью урока",
    )

    video_url = EmbedVideoField()

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
