from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from NCPWD.apps.user_profile.serializers import ProfileSerializer, DisabilitySerializer
from NCPWD.permission import IsOwnerOrReadOnly
from .models import  Profile, Disability

# Create your views here.


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet
                     ):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class DisabilityViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DisabilitySerializer
    queryset = Disability.objects.all()

