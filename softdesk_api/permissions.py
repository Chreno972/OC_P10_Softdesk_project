"""_summary_

Returns:
    _type_: _description_
"""
from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):
    """_summary_"""

    def has_permission(self, request, view):
        """_summary_"""

        return bool(
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class IsContributorAuthenticated(BasePermission):
    """_summary_"""

    def has_permission(self, request, view):
        """_summary_"""

        return bool(
            request.user and request.user.is_authenticated and request.user.is_contributor
        )
