# Generated by Django 4.2 on 2024-07-16 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0011_alter_habit_time_spent"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="associated_habit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="habits.habit",
                verbose_name="Связанная привычка",
            ),
        ),
    ]
