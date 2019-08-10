from django.db import models
from NCPWD.apps.authentication.models import User


class Profile(models.Model):
    sex_choices = [
        ("MALE", "male"),
        ("FEMALE", "female")
    ]
    cause_choices = [
        ("ILLNESS", 'illness'),
        ("BIRTH", 'birth'),
        ("ACCIDENT", 'accident'),
    ]
    disability_choices = [
        ("ALBINISM", 'albinism'),
        ("PHYSICAL", 'physical'),
        ("MENATL", 'mental'),
        ("VISUAL", 'visual'),
        ("HEARING", 'hearing'),
        ("EPILEPSY", 'epilepsy'),
        ("BLIND", 'blind')

    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(
        max_length=20, default="firstname", null=True, blank=True)
    lastname = models.CharField(
        max_length=20, default="lastname", null=True, blank=True)
    email = models.EmailField(default="email", null=True, blank=True)
    national_id = models.CharField(
        max_length=20, default="national id", null=True, blank=True)
    phone = models.CharField(
        max_length=15, default="phone number", null=True, blank=True)
    location = models.CharField(
        max_length=30, default="location", null=True, blank=True)
    nationality = models.CharField(
        max_length=40, default="nationality", null=True, blank=True)
    sex = models.CharField(
        max_length=10, default="sex",
        choices=sex_choices, null=True, blank=True)
    date_of_birth = models.DateField(
        default="1996-06-06", null=True, blank=True)
    disability = models.CharField(
        max_length=15, choices=disability_choices,
        default="ALBINISM", null=True, blank=True)
    cause = models.CharField(
        max_length=10, choices=cause_choices,
        default="BIRTH", null=True, blank=True)
