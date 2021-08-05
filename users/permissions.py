''' User editing permission '''

#Django REST framework
from rest_framework.permissions import BasePermission

#Models
from django.contrib.auth.models import User
from users.models import Profile

class IsOwnProfile(BasePermission):
    ''' Check if the user try to edit its own template '''

    def has_object_permission(self, request, view, abj):
        try:
            User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            return False
        
        return True