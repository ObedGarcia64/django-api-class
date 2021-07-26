""" Account verification serializerv """

#django
from django.conf import settings

#django REST frameowrk
from rest_framework import serializers

#model
from django.contrib.auth.models import User

#utilities
import jwt

class AccountVerificationSerializer(serializers.Serializer):
    """ACCOUNT VERIFICATION SERIALIZER """

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token in valid """

        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError({'Error': 'Verification link has expired'})
        except jwt.PyJWKError:
            raise serializers.ValidationError({'Error': 'Invalid token'})

        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError({'Error': 'Invalid token'})

        self.context['payload'] = payload

        return data

    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.profile.is_verified = True
        user.profile.save()
        return user