from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.pagination import MyPagination
from habits.serialaizers import HabitSerializer
from users.permissions import IsOwner, IsPublic


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def list(self, request):
        queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class HabitListApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = (IsPublic,)
    pagination_class = MyPagination
