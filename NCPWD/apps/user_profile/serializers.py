from rest_framework.serializers import (
    ModelSerializer, CharField, DateField, ValidationError
)
from NCPWD.apps.user_profile.models import Profile, Disability


class ProfileSerializer(ModelSerializer):
    national_id = CharField(required=True)
    phone = CharField(required=True)
    location = CharField(required=True)
    national_id = CharField(required=True)
    date_of_birth = DateField(required=True)

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

    def validate_phone(self, phone):
        try:
            int(phone)
        except ValueError:
            raise ValidationError(
                {"phone": "must be a number"}
            )





class DisabilitySerializer(ModelSerializer):
    class Meta:
        model = Disability
        fields = "__all__"
