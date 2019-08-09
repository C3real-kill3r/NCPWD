from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from NCPWD.apps.user_profile.serializers import (
    ProfileSerializer)
from NCPWD.permission import IsOwnerOrReadOnly
from .models import Profile
from NCPWD.apps.core.exceptions import ProfileDoesNotExist


class ProfileListView(ListAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a listing of user profiles. Excludes the requester.
        """
        try:
            queryset = Profile.objects.all().exclude(user=request.user)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyProfile(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a listing of user profiles. Excludes the requester.
        """
        try:
            queryset = Profile.objects.filter(user=request.user)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Allows authenticated users to update only their profiles."""
        try:
            Profile.objects.filter(user__username=request.user)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        data = request.data

        serializer = self.serializer_class(
            instance=request.user.profile, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileGetView(APIView):
    """Lists fetches a single profile and also updates a specific profile"""

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer

    def get(self, request, username):
        """Fetches a specific profile filtered by the username"""

        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
