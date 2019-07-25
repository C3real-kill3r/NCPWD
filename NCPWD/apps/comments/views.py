from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
from NCPWD.permission import IsOwnerOrReadOnly
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin,
    ListModelMixin, RetrieveModelMixin
    )
from .models import Comments
from .serializers import CommentSerializer


class CommentViewSet(
        CreateModelMixin, DestroyModelMixin,
        ListModelMixin, RetrieveModelMixin,
        GenericViewSet
                    ):

    queryset = Comments.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer


class TopicCommentAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        topic = self.kwargs["topic"]
        return Comments.objects.filter(topic=topic)
