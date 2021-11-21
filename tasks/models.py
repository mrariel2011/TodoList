from django.db import models
from django.utils import timezone


class Task(models.Model):

    title = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    due_to = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
