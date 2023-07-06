from rest_framework import permissions

from user.models import RoleChoice


class IsShipper(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == RoleChoice.shipper)


class IsDriver(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == RoleChoice.driver)


class IsCompanyAdmin(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == RoleChoice.company_admin)


class IsSuperuser(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and
                    request.user.role == RoleChoice.superuser and request.user.is_superuser)
