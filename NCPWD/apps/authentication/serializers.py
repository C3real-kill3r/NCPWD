import re

from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from NCPWD.apps.core import validations


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
    )
    email = serializers.EmailField(
        required=True,
        error_messages={
            "required": "Email is required!"
        }
    )
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=True,
    )
    token = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def validate_username(self, data):
        candidate_name = data
        try:
            if int(candidate_name):
                raise serializers.ValidationError(
                    {"username": ["Username cannot be numbers only!"]})
        except ValueError:
            pass
        if candidate_name == "":
            raise serializers.ValidationError(
                {"username": ["Username is required!"]})
        elif User.objects.filter(username=candidate_name):
            raise serializers.ValidationError(
                {"username": ["Username already exists!"]})
        elif len(candidate_name) < 4:
            raise serializers.ValidationError(
                {"username": ["Username should be more than 4 charcaters!"]})
        elif len(candidate_name) > 128:
            raise serializers.ValidationError(
                {"username": ["Username should not be longer than 128 charcaters!"]})
        return data

    def validate_email(self, data):
        candidate_email = data
        if candidate_email == "":
            raise serializers.ValidationError({"email": ["Email is required!"]})
        elif re.match(validations.trial_email, candidate_email):
            raise serializers.ValidationError(
                {"email": ["Invalid email! Hint: example@mail.com"]})
        elif re.match(validations.trial_email_2, candidate_email):
            raise serializers.ValidationError(
                {"email": ["Invalid email! Hint: example@mail.com"]})
        elif User.objects.filter(email=candidate_email):
            raise serializers.ValidationError(
                {"email": ["User with provided email exists! Please login!"]})
        elif not re.match(validations.email_expression, candidate_email):
            raise serializers.ValidationError(
                {"email": ["Invalid email! Hint: example@mail.com!"]})
        return data

    def validate_password(self, data):
        candidate_password = data
        if candidate_password == "":
            raise serializers.ValidationError({
                "password": ["Password is required!"]})
        elif len(candidate_password) < 8:
            raise serializers.ValidationError({
                "password": ["Password should be at least eight (8) characters long!"]})
        elif len(candidate_password) > 128:
            raise serializers.ValidationError({
                "password": ["Password should not be longer than (128) characters long!"]})
        elif not re.match(validations.at_least_number, candidate_password):
            raise serializers.ValidationError({
                "password": ["Password must have at least one number!"]})
        elif not re.match(validations.at_least_uppercase, candidate_password):
            raise serializers.ValidationError({
                "password": ["Password must have at least one uppercase and lowercase letter!"]})
        elif not re.match(validations.at_least_special_char, candidate_password):
            raise serializers.ValidationError({
                "password": ["Password must include a special character!"]})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=512, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This account has been deactivated.'
            )

        if not user.is_verified:
            raise serializers.ValidationError(
                'Check your email to verify the account.'
                )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token,

        }


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255)

    def validate(self, data):
        email = data.get('email')
        user = User.objects.filter(email=email).first()
        if data.get('password') != data.get('confirm_password'):
            msg = "The passwords do not match."
            raise serializers.ValidationError(msg)
        token = data.get('token')
        validate_token = default_token_generator.check_token(user, token)
        if not validate_token:
            msg = "The link has expried, kindly request for another reset."
            raise serializers.ValidationError(msg)
        user.set_password(data.get('password'))
        user.save()
        return data
