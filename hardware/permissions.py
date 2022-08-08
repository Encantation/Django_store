from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    '''Permission to view if SAFE_METHODS and delete if user is admin '''
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Permission to view if SAFE_METHODS and delete if object posted by this user'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
