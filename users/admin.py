from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "tg_chat_id",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    search_fields = ("email", "tg_chat_id")
    list_filter = ("is_staff", "is_superuser", "is_active")
