from django.db import models
from NCPWD.apps.authentication.models import User


class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
