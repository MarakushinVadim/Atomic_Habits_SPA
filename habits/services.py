from datetime import timedelta

import requests

from Atomic_Habits_SPA.settings import BOT_TOKEN, TG_URL


def create_timedelta(frequency):
    """Функция создания timedelta, для периодичности привычки"""
    if frequency == "daily":
        return timedelta(days=1)
    elif frequency == "every_two_days":
        return timedelta(days=2)
    elif frequency == "every_three_days":
        return timedelta(days=3)
    elif frequency == "every_four_days":
        return timedelta(days=4)
    elif frequency == "every_five_days":
        return timedelta(days=5)
    elif frequency == "every_six_days":
        return timedelta(days=6)
    elif frequency == "weekly":
        return timedelta(weeks=1)


def send_tg_message(text, chat_id):
    """Функция отправки сообщения в Telegram"""
    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(f"{TG_URL}{BOT_TOKEN}/sendMessage", params=params)
