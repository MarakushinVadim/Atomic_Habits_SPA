from datetime import timedelta

from rest_framework.serializers import ValidationError


class NotTwiceRewardValidator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __call__(self, habit):
        if habit.get("associated_habit") and habit.get("reward"):
            raise ValidationError(
                "Необходимо выбрать или только приятную привычку, или только награду"
            )
        if not habit.get("associated_habit") and not habit.get("reward"):
            raise ValidationError(
                "Необходимо выбрать награду"
            )


class NoRewardNiceHabitValidator:
    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __call__(self, habit):
        if habit.get("is_nice_habit"):
            if habit.get("reward"):
                raise ValidationError(
                    "У приятной привычки не может быть награды"
                )
            if habit.get("associated_habit"):
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки"
                )


class NoForeignHabitValidator:

    def __init__(self, value1):
        self.value1 = value1

    def __call__(self, habit):
        associated_habit = habit.get("associated_habit")
        if associated_habit:
            if not associated_habit.is_nice_habit:
                raise ValidationError(
                    "Связанная привычка должна быть приятной"
                )


class DurationValidator:
    def __init__(self, value1):
        self.value1 = value1

    def __call__(self, habit):
        if habit.get("time_spent") > timedelta(seconds=120):
            raise ValidationError(
                "Время затрачиваемое на привычку не может превышать 2 минуты"
            )
