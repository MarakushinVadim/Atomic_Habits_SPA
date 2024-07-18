from datetime import datetime, time

from celery import shared_task
import django.utils.timezone


from habits.models import Habit


# @shared_task
# def send_reminder():
#     reminder_today = Habit.objects.all().filter(start_date=django.utils.timezone.localdate())
#     print(reminder_today)
#
#     if reminder_today.exists():
#         for habit in reminder_today:
#             current_time = time.now(pytz.timezone("Europe/Moscow"))
#             if habit.start_time > datetime.time.