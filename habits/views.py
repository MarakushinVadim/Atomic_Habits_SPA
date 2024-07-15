from rest_framework.viewsets import ModelViewSet

from habits.models import Habit, EnjoyableHabit
from habits.serialaizers import HabitSerializer, EnjoyableHabitSerializer


class EnjoyableHabitViewSet(ModelViewSet):
    queryset = EnjoyableHabit.objects.all()
    serializer_class = EnjoyableHabitSerializer

    def perform_create(self, serializer):
        enjoyable_habit = serializer.save()
        enjoyable_habit.user = self.request.user
        enjoyable_habit.save()


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()
