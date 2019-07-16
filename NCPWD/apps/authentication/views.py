import os

# Create your views here.
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from NCPWD.apps.authentication.serializers import (
    RegistrationSerializer, LoginSerializer)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .models import User
from NCPWD.apps.core import client


class RegistrationAPIView(CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.validate_username(user["username"])
        serializer.validate_email(user["email"])
        serializer.validate_password(user["password"])

        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.filter(email=user['email']).first()

        RegistrationAPIView.send_account_activation_email(user, request)

        data = serializer.data
        data['message'] = 'Check your email to activate your account'
        return Response(data, status=status.HTTP_201_CREATED)

    @staticmethod
    def send_account_activation_email(user, request=None, send_email=True):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.username))

        if send_email:
            email = user.email
            username = user.username
            from_email = os.getenv("EMAIL_HOST_SENDER")

            email_subject = 'Activate your NCPWD account.'
            email_message = render_to_string('email_verification.html', {
                'activation_link': client.get_activation_link(token, uid),
                'title': email_subject,
                'username': username
            })
            text_content = strip_tags(email_message)
            msg = EmailMultiAlternatives(
                email_subject, text_content, from_email, to=[email])
            msg.attach_alternative(email_message, "text/html")
            msg.send()

        return token, uid


class LoginAPIView(CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=user['email'])
        resp = {
            "token": serializer.data['token']
        }

        return Response(resp, status=status.HTTP_200_OK)


class AccountVerificationView(APIView):
    permission_classes = AllowAny,

    def get(self, request, token, uid):
        username = force_text(urlsafe_base64_decode(uid))

        user = User.objects.filter(username=username).first()
        validate_token = default_token_generator.check_token(user, token)

        data = {"message": "Your account has been successfully activated!!"}
        res = status.HTTP_200_OK

        if not validate_token:
            data['message'] = "Your link is either Invalid or has expired."
            res = status.HTTP_400_BAD_REQUEST
        else:
            user.is_verified = True
            user.save()

        return Response(data, status=res)
