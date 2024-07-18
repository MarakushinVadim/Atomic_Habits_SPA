from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "start_date", "start_time", "frequency", "user", "is_nice_habit")
    search_fields = ("title", "description", "user")
    list_filter = ("start_date", "frequency", "user")
