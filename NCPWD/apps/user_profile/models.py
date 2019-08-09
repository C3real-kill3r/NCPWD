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
    firstname = models.CharField(max_length=20, default="firstname")
    lastname = models.CharField(max_length=20, default="lastname")
    email = models.EmailField(default="email")
    national_id = models.CharField(max_length=20, default="national id")
    phone = models.CharField(max_length=15, default="phone number")
    location = models.CharField(max_length=30, default="location")
    nationality = models.CharField(max_length=40, default="nationality")
    sex = models.CharField(max_length=10, default="sex", choices=sex_choices)
    date_of_birth = models.DateField(default="1996-06-06")
    disability = models.CharField(
        max_length=15, choices=disability_choices, default="ALBINISM")
    cause = models.CharField(
        max_length=10, choices=cause_choices, default="BIRTH")
