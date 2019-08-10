from rest_framework.serializers import (
    ModelSerializer, CharField, DateField, ValidationError,
)

from NCPWD.apps.user_profile.models import Profile


class ProfileSerializer(ModelSerializer):
    national_id = CharField(required=True)
    firstname = CharField(required=True)
    email = CharField(required=True)
    lastname = CharField(required=True)
    phone = CharField(required=True)
    location = CharField(required=True)
    nationality = CharField(required=True)
    date_of_birth = DateField(required=True)
    disability = CharField(required=True)
    cause = CharField(required=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

    def to_representation(self, instance):
        ret = {
            "id": instance.id,
            "user": instance.user.id,
            "phone": instance.phone,
            "email": instance.email,
            "location": instance.location,
            "national_id": instance.national_id,
            "date_of_birth": instance.date_of_birth,
            "nationality": instance.nationality,
            "firstname": instance.firstname,
            "lastname": instance.lastname,
            "sex": instance.sex,
            "disability": instance.disability,
            "cause": instance.cause,
        }
        return ret

    def update(self, instance, validated_data):
        instance.location = validated_data.get("location", instance.location)
        instance.national_id = validated_data.get(
            "national_id", instance.national_id)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.firstname = validated_data.get(
            "firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.email = validated_data.get("email", instance.email)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth)
        instance.nationality = validated_data.get(
            "nationality", instance.nationality)
        instance.sex = validated_data.get("sex", instance.sex)
        instance.disability = validated_data.get(
            "disability", instance.disability)
        instance.cause = validated_data.get("cause", instance.cause)

        instance.save()
        return instance
