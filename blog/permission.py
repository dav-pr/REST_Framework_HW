from rest_framework import permissions

class isAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.author.name == request.user.username
