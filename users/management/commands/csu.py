from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомый команда создания администратора"""

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@admin.ru")
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password("123qwe")
        user.save()
