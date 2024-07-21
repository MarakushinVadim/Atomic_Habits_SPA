from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Контролирует доступ к объекту только для его создателя."""

    def has_object_permission(self, request, view, obj):
        if obj:
            if obj.user == request.user:
                return True
            return False
