from rest_framework import serializers
from .models import Topic
from NCPWD.apps.user_profile.serializers import ProfileSerializer
from NCPWD.apps.user_profile.models import Profile


class TopicSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        required=True,
        max_length=255,
        allow_blank=False,
        error_messages={
            'blank': 'The Topic must have a title',
            'required': "The topic must have a title",
            'max_length':
                "The article topiv cannot be more than 255 characters"
        })
    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'The topic must have a description',
            'required': "The topic must have a description",
        })

    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        serializer = ProfileSerializer(
            instance=Profile.objects.get(user=obj.author))
        return serializer.data

    class Meta:
        model = Topic
        fields = "__all__"
        read_only_fields = ('author',)

    def create(self, validated_data):
        topic = Topic.objects.create(**validated_data)

        return topic

    def update(self, instance, validated_data):

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
