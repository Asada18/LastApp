from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Post
from .serializers import *
from django.core.mail import send_mail


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                user.create_activation_code()
                send_activation_code(user.email, user.activation_code)
                return Response(serializer.data, status=status.HTTP_200_OK)


class ActivateView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.activate_with_code(activation_code)
        # user.is_active = True
        # user.activation_code = ''
        # user.save()
        return Response(data={'message': 'Аккаунт успешно активирован'}, status=status.HTTP_200_OK)

        # return Response("Your account successfully activated!", status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logged out', status=status.HTTP_200_OK)













































