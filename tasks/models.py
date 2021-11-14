from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    due_to = models.DateTimeField()
    done = models.BooleanField(default=False)
