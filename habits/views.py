from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.pagination import MyPagination
from habits.serialaizers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """Вью сет для привычек, для работы необходима авторизация"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        """Сохраняет привычку с авторизованным пользователем"""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def list(self, request):
        """Отображает привычки текущего пользователя"""
        queryset = Habit.objects.filter(user=request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        """Проверяет разрешения для действий"""
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif (
            self.action == "update"
            or self.action == "partial_update"
            or self.action == "destroy"
        ):
            self.permission_classes = (IsOwner,)
        elif self.action == "list" or self.action == "retrieve":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class HabitListAPIView(ListAPIView):
    """ "Отображает публичные привычки"""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
