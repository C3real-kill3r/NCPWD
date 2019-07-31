from rest_framework.serializers import (
    ModelSerializer, CharField, DateField, ValidationError
)

from NCPWD.apps.user_profile.models import Profile, Disability, UserDisability


class UserDisabilitySerializer(ModelSerializer):
    class Meta:
        model = UserDisability
        exclude = ["profile"]


class ProfileSerializer(ModelSerializer):
    national_id = CharField(required=True)
    firstname = CharField(required=True)
    lastname = CharField(required=True)
    phone = CharField(required=True)
    location = CharField(required=True)
    nationality = CharField(required=True)
    date_of_birth = DateField(required=True)
    disabilities = UserDisabilitySerializer(many=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

    def validate_national_id(self, national_id):
        try:
            int(national_id)
        except ValueError:
            raise ValidationError(
                {"national_id": "must be a number"}
            )
        return national_id

    def validate_phone(self, phone):
        try:
            int(phone)
        except ValueError:
            raise ValidationError(
                {"phone": "must be a number"}
            )

        return phone

    def to_representation(self, instance):
        ret = {
            "id": instance.id,
            "user": instance.user.id,
            "phone": instance.phone,
            "location": instance.location,
            "national_id": instance.national_id,
            "date_of_birth": instance.date_of_birth,
            "nationality": instance.nationality,
            "firstname": instance.firstname,
            "lastname": instance.lastname,
            "sex": instance.sex,
            "disabilities": []
        }

        disabilities = UserDisability.objects.filter(profile=instance)
        for i in disabilities:
            disab = {
                "id": i.id,
                "profile": i.profile.id,
                "disability": i.disability.id,
                "cause": i.cause
            }
            ret["disabilities"].append(disab)
        return ret

    def update(self, instance, validated_data):
        instance.location = validated_data.get("location", instance.location)
        instance.national_id = validated_data.get(
            "national_id", instance.national_id)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth)
        instance.nationality = validated_data.get(
            "nationality", instance.nationality)
        instance.sex = validated_data.get("sex", instance.sex)
        update_disabilities = list(validated_data.get("disabilities"))
        for i in UserDisability.objects.filter(profile=instance):
            i.delete()
        for i in update_disabilities:
            UserDisability(**dict(i), profile=instance).save()

        instance.save()
        return instance


class DisabilitySerializer(ModelSerializer):
    class Meta:
        model = Disability
        fields = "__all__"
