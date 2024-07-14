from rest_framework import serializers

from habits.models import Habit, EnjoyableHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class EnjoyableHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnjoyableHabit
        fields = "__all__"
