from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _

class LoginSerializer(serializers.Serializer):
    """login serializer
    """

    user = None

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(LoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        """ validate email credentials
        """
        email, password = data.values()

        if not email or not password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        self.user = authenticate(request=self.request,
            email=email, password=password)
        
        if not self.user:
            msg = _('Invalid email or password')
            raise serializers.ValidationError(msg, code='authorization')

        
        return data


