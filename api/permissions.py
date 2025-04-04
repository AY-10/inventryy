from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    """
    Custom permission to only allow super admins to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'super_admin'


class IsAdmin(BasePermission):
    """
    Custom permission to only allow admins to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'
