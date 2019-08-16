from django.db import models
from NCPWD.apps.authentication.models import User


class Profile(models.Model):
    sex_choices = [
        ("MALE", "male"),
        ("FEMALE", "female")
    ]
    type_choices = [
        ("A", 'a'),
        ("B", 'b'),
        ("AB", 'ab'),
        ("O", 'o')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=15, default="phone number", null=True, blank=True)
    location = models.CharField(
        max_length=30, default="location", null=True, blank=True)
    sex = models.CharField(
        max_length=10, default="sex",
        choices=sex_choices, null=True, blank=True)
    date_of_birth = models.DateField(
        default="1996-06-06", null=True, blank=True)
    blood_type = models.CharField(
        max_length=15, choices=type_choices,
        default="blood type", null=True, blank=True)
