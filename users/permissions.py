''' User editing permission '''

#Django REST framework
from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token

#Models
from django.contrib.auth.models import User
from users.models import Profile

class IsOwnProfile(BasePermission):
    ''' Check if the user try to edit its own template '''

    def has_object_permission(self, request, view, abj):
        
        token = request.headers['Authorization']
        token = token.split(' ')
        token = Token.objects.get(key=token[1])
        print(request)
        
        try:
            User.objects.get(username=request.user.username)
            #Token.objects.get()
        except User.DoesNotExist:
            return False
        
        return True