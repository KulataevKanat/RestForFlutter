from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    try:
        return Group \
            .objects \
            .get(name=group_name) \
            .user_set.filter(id=user.id) \
            .exists()

    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any(
        [
            _is_in_group(
                user,
                group_name
            )
            for group_name in required_groups
        ]
    )


class ROLE_ADMIN(permissions.BasePermission):
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class ROLE_USER(permissions.BasePermission):
    required_groups = ['user']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class AllowAnyGroups(permissions.BasePermission):
    required_groups = ['admin', 'user']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class UserPermissionsObj(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return request.user.__eq__(obj)
