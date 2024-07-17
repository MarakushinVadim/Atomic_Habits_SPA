from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj:
            if obj.user == request.user:
                return True
            return False


class IsPublic(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.data)
        return request.habit.filter(is_public=True).all()
