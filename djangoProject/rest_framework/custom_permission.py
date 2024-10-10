from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.path.startswith('/api/publish'):
            return True
        return request.user and request.user.is_authenticated
