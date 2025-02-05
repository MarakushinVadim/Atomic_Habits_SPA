# Generated by Django 4.2 on 2024-07-15 06:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("habits", "0003_alter_enjoyablehabit_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enjoyablehabit",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель привычки",
            ),
        ),
    ]
