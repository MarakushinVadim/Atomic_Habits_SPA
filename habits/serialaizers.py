from rest_framework import serializers

from habits.models import Habit
from habits.validators import (DurationValidator, NoForeignHabitValidator,
                               NoRewardNiceHabitValidator,
                               NotTwiceRewardValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

        validators = [
            NotTwiceRewardValidator(
                "associated_habit",
                "reward",
                "is_nice_habit"
            ),
            NoRewardNiceHabitValidator(
                "is_nice_habit",
                "reward",
                "associated_habit"
            ),
            NoForeignHabitValidator("associated_habit"),
            DurationValidator("time_spent"),
        ]
