from rest_framework.viewsets import ModelViewSet
from NCPWD.permission import IsAdmin
from .models import Topic
from .serializers import TopicSerilizer


class TopicViewSet(ModelViewSet):
    permission_classes = (IsAdmin,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerilizer

