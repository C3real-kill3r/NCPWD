from django.db import models
from NCPWD.apps.authentication.models import User


class Disability(models.Model):
    detail = models.TextField()


class Profile(models.Model):
    sex_choices = [
        ("MALE", "male"),
        ("FEMALE", "female")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, default="placeholder")
    lastname = models.CharField(max_length=20, default="placeholder")
    national_id = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=40, null=True)
    sex = models.CharField(max_length=10, null=True, choices=sex_choices)
    date_of_birth = models.DateField(null=True)
    disabilities = models.ManyToManyField(Disability, blank=True, through='UserDisability')


class UserDisability(models.Model):
    cause_choices = [
        ("ILLNESS", 'illness'),
        ("BIRTH", 'birth'),
        ("ACCIDENT", 'accident'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE)
    cause = models.CharField(max_length=10, choices=cause_choices)







