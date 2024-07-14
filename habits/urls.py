from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, EnjoyableHabitViewSet

app_name = HabitsConfig.name

router = routers.DefaultRouter()
router.register(r"enjoyable", EnjoyableHabitViewSet, basename="enjoyable")
router.register(r"habits", HabitViewSet, basename="habits")
urlpatterns = []
urlpatterns += router.urls
