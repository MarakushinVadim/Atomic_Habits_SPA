from rest_framework import serializers

from habits.models import Habit, EnjoyableHabit
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    nice_habits = serializers.
    class Meta:
        model = Habit
        fields = "__all__"


class EnjoyableHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnjoyableHabit
        fields = "__all__"
