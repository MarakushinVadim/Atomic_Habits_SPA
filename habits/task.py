from datetime import datetime

import pytz
from celery import shared_task
import django.utils.timezone


from habits.models import Habit
from habits.services import create_timedelta, send_tg_message


@shared_task
def send_reminder():
    reminder_today = Habit.objects.filter(start_date=django.utils.timezone.localdate())
    print(reminder_today)

    if reminder_today:
        for habit in reminder_today:
            current_datetime = datetime.now(pytz.timezone("Europe/Moscow"))
            habit_datetime = datetime.combine(habit.start_date, habit.start_time)
            if current_datetime > habit_datetime:
                print(f"У вас есть напоминание о привычке: {habit}")
                habit.start_date = habit.start_date + create_timedelta(habit.frequency)
                habit.save()
                if habit.user.tg_chat_id:
                    send_tg_message(f"У вас есть напоминание о привычке: {habit}", habit.user.tg_chat_id)
