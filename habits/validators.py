from rest_framework.serializers import ValidationError


def validate_habit(nice_habit, reward):
    if nice_habit is not None and reward is not None:
        return ValidationError("Можно выбрать только приятную привычку или только награду")
    if nice_habit is None and reward is None:
        return ValidationError("Необходимо выбрать приятную привычку или награду")
