import datetime
from datetime import timedelta

import django.utils.timezone
from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    class FrequencyChoices(models.TextChoices):
        DAILY = "daily", "Ежедневно"
        EVERY_TWO_DAYS = "every_two_days", "Каждые два дня"
        EVERY_THREE_DAYS = "every_three_days", "Каждые три дня"
        EVERY_FOUR_DAYS = "every_four_days", "Каждые четыре дня"
        EVERY_FIVE_DAYS = "every_five_days", "Каждые пять дней"
        EVERY_SIX_DAYS = "every_six_days", "Каждые шесть дней"
        WEEKLY = "weekly", "Еженедельно"

    name = models.CharField(
        max_length=255,
        verbose_name="Название привычки",
        help_text="введите название привычки",
    )
    description = models.TextField(
        verbose_name="Описание привычки", help_text="введите описание привычки"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель привычки", **NULLABLE
    )
    place = models.CharField(
        max_length=255, verbose_name="место", help_text="введите место привычки"
    )
    frequency = models.CharField(
        max_length=16,
        default=FrequencyChoices.DAILY,
        choices=FrequencyChoices.choices,
        verbose_name="Периодичность привычки",
    )
    start_time = models.TimeField(verbose_name="Время начала привычки")
    action = models.CharField(
        max_length=100,
        verbose_name="Действие привычки",
        help_text="введите действие привычки",
    )
    is_nice_habit = models.BooleanField(default=False, verbose_name="Хорошая привычка")
    reward = models.CharField(
        max_length=255, verbose_name="Награда за выполнение привычки", **NULLABLE
    )
    associated_habit = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Связанная привычка",
                                         **NULLABLE)
    time_spent = models.DurationField(default=timedelta(seconds=120),
                                      verbose_name="Время затрачиваемое на привычку"
                                      )
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")
    start_date = models.DateField(default=django.utils.timezone.localdate(), verbose_name='Дата выполнения')

    def __str__(self):
        return f"Я буду {self.action} в {self.start_time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
