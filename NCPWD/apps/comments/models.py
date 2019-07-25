from django.db import models
from NCPWD.apps.topics.models import Topic
from datetime import datetime
from NCPWD.apps.authentication.models import User


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)



