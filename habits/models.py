from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class EnjoyableHabit(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название приятной привычки",
        help_text="введите название приятной привычки",
    )
    description = models.TextField(
        verbose_name="Описание приятной привычки",
        help_text="введите описание приятной привычки",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель привычки"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятная привычки"


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
        User, on_delete=models.CASCADE, verbose_name="Создатель привычки"
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
    nice_habit = models.ForeignKey(
        EnjoyableHabit,
        on_delete=models.CASCADE,
        verbose_name="Приятная привычка",
        **NULLABLE,
    )
    reward = models.CharField(
        max_length=255, verbose_name="Награда за выполнение привычки", **NULLABLE
    )
    time_spent = models.DurationField(
        verbose_name="Время затрачиваемое на привычку", **NULLABLE
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    def __str__(self):
        return f"Я буду {self.action} в {self.start_time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
