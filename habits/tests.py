from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="testuser",
            password="testpass",
            tg_chat_id="214753124",
        )
        self.client.force_authenticate(user=self.user)
        print(self.user.id)

    def test_create_habit(self):
        data = {
            "name": "Test Habit",
            "description": "This is a test habit",
            "category": "Work",
            "frequency": "daily",
            "start_time": "12:55:00",
            "place": "test_place",
            "action": "test_action",
            "time_spent": 70,
            "is_public": True,
            "start_date": "2022-01-01",
            "associated_habit": "",
            "reward": "test_reward",
        }
        responce = self.client.post("/habits/", data=data)
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        test_data = {
            "id": 1,
            "name": "Test Habit",
            "description": "This is a test habit",
            "place": "test_place",
            "frequency": "daily",
            "start_time": "12:55:00",
            "action": "test_action",
            "is_nice_habit": False,
            "reward": "test_reward",
            "time_spent": "00:01:10",
            "is_public": True,
            "start_date": "2022-01-01",
            "user": 1,
            "associated_habit": None,
        }
        self.assertEqual(responce.json(), test_data)
        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):
        test_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 2,
                    "name": "Test Habit",
                    "description": "This is a test habit",
                    "place": "test_place",
                    "frequency": "daily",
                    "start_time": "12:55:00",
                    "action": "test_action",
                    "is_nice_habit": False,
                    "reward": "test_reward",
                    "time_spent": "00:01:10",
                    "is_public": True,
                    "start_date": "2022-01-01",
                    "user": None,
                    "associated_habit": None,
                }
            ],
        }

        Habit.objects.create(
            name="Test Habit",
            description="This is a test habit",
            frequency="daily",
            start_time="12:55:00",
            place="test_place",
            action="test_action",
            time_spent="70",
            is_public=True,
            start_date="2022-01-01",
            associated_habit=None,
            reward="test_reward",
        )
        responce = self.client.get("/habits/")

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json(), test_data)
