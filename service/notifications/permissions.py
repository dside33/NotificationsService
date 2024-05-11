from rest_framework.permissions import BasePermission

from userprofile.models import APIKey


class HasAPIKeyAndIsAuthenticated(BasePermission):
    message = 'пошел отсюда вон.'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        api_key = request.headers.get('Authorization')

        if not api_key:
            return False

        return APIKey.objects.filter(value=api_key, user=request.user).exists()
    