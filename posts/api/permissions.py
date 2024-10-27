from rest_framework.permissions import BasePermission

class PostPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif request.method == 'GET':
            return True
        elif (request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE'):
            return request.user == obj.user
