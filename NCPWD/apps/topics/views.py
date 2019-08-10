from NCPWD.permission import IsAdmin, IsOwnerOrReadOnly
from .models import Topic
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopicSerializer


class TopicAPIView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin): # noqa

    lookup_url_kwarg = 'pk'
    permission_classes = (IsAdmin, IsOwnerOrReadOnly)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def create(self, request, *args, **kwargs):

        topic = request.data
        serializer = self.serializer_class(data=topic)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, **kwargs):
        pk = self.kwargs.get('pk')
        topic = Topic.objects.filter(pk=pk)
        if topic.count() < 1:
            return Response({
                'errors': 'Topic does not exist'
            }, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            topic, context={'request': request}, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        topic = Topic.objects.filter(pk=pk).first()
        if topic is None:
            return Response({
                'errors': 'Topic does not exist'
            }, status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            topic, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
