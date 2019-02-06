from .models import User
from rest_framework import viewsets
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer, RegisterSerializer
from .managers import UserManager
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class Login(APIView):
    """login
    """
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self,*args,**kwargs):
        serializer = self.serializer_class(
            data=self.request.data, request=self.request)

        serializer.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(user=serializer.user)

        return Response({
            'token': token.key,
        }, status=200, headers={'Authorization': 'Token {}'.format(token.key)})


class Register(APIView):
    """register
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(
            data=self.request.data)
        
        serializer.is_valid(raise_exception=True)
    
        user = serializer.save()
        user.set_password(serializer.data['password'])  
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
        }, status=200, headers={'Authorization': 'Token {}'.format(token.key)})


class RefreshToken(APIView):
    """refresh token
    """
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        
        user = authenticate(
            username=request.data['email'],
            password=request.data['password']
        )
        token = Token.objects.get(user=user)
        
        return Response({
            'token': token.key
        }, status=200, headers={'Authorization': 'Token {}'.format(token.key)})










