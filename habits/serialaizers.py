from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    # nice_habit, reward = serializers.CharField(validators=[validate_habit])

    class Meta:
        model = Habit
        fields = "__all__"
