from rest_framework.viewsets import ModelViewSet

from habits.models import Habit, EnjoyableHabit
from habits.serialaizers import HabitSerializer, EnjoyableHabitSerializer


class EnjoyableHabitViewSet(ModelViewSet):
    queryset = EnjoyableHabit.objects.all()
    serializer_class = EnjoyableHabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
