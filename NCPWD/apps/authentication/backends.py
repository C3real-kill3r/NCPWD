import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request)
        if not token:
            return None;

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)

        except jwt.exceptions.DecodeError:
            raise AuthenticationFailed("Invalid Token")
        user = User.objects.get(username=payload.get("username"))

        if not user:
            raise AuthenticationFailed("No user found for provided token")

        if not user.is_active:
            raise AuthenticationFailed("Inactive user. Kindly activate")

        return user, token
