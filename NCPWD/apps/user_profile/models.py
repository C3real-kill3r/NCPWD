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
    firstname = models.CharField(max_length=20, default="firstname")
    lastname = models.CharField(max_length=20, default="lastname")
    email = models.EmailField(default="email")
    national_id = models.CharField(max_length=20, default="national id")
    phone = models.CharField(max_length=15, default="phone number")
    location = models.CharField(max_length=30, default="location")
    nationality = models.CharField(max_length=40, default="nationality")
    sex = models.CharField(max_length=10, default="sex", choices=sex_choices)
    date_of_birth = models.DateField(default="1996-06-06")
    disabilities = models.ManyToManyField(
        Disability, blank=True, through='UserDisability')


class UserDisability(models.Model):
    cause_choices = [
        ("ILLNESS", 'illness'),
        ("BIRTH", 'birth'),
        ("ACCIDENT", 'accident'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE)
    cause = models.CharField(max_length=10, choices=cause_choices)
