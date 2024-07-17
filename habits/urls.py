from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, HabitListAPIView

app_name = HabitsConfig.name

router = routers.DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")
urlpatterns = [
    path("public_list/", HabitListAPIView.as_view()),
]
urlpatterns += router.urls
