from rest_framework import permissions
from rest_framework.permissions import BasePermission


class UpdateOwnProfile(BasePermission):
    """
    Allow users to update their own profile
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if user is trying to update his own profile
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        # if this is not safe method check if the user is trying to update
        # his own profile
        return obj.id == request.user.id


class PostOwnStatus(BasePermission):
    """ Allow users to uodate their own status """

    def has_object_permission(self, request, view, obj):
        """
        Check if user is trying to update his own status
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        # if this is not safe method check if the user is trying to update
        # his own status
        return obj.user_profile.id == request.user.id
