from rest_framework.serializers import ModelSerializer
from .models import Topic


class TopicSerilizer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
