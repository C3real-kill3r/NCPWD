from rest_framework.serializers import (
    ModelSerializer, CharField, DateField,
)

from NCPWD.apps.user_profile.models import Profile


class ProfileSerializer(ModelSerializer):
    phone = CharField(required=True)
    location = CharField(required=True)
    sex = CharField(required=True)
    date_of_birth = DateField(required=True)
    blood_type = CharField(required=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

    def to_representation(self, instance):
        ret = {
            "id": instance.id,
            "user": instance.user.id,
            "username": instance.user.username,
            "email": instance.user.email,
            "phone": instance.phone,
            "location": instance.location,
            "date_of_birth": instance.date_of_birth,
            "sex": instance.sex,
            "blood_type": instance.blood_type,
        }
        return ret

    def update(self, instance, validated_data):
        instance.location = validated_data.get("location", instance.location)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.user.username = validated_data.get(
            "username", instance.user.username)
        instance.user.email = validated_data.get(
            "email", instance.user.email)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth)
        instance.sex = validated_data.get("sex", instance.sex)
        instance.blood_type = validated_data.get(
            "blood_type", instance.blood_type)

        instance.save()
        return instance
