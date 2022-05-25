from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return "{} ({})".format(self.name, self.id)


class Task(models.Model):

    title = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    due_to = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} ({})".format(self.title, self.id)

    @property
    def due_to_iso(self):
        data_formatted = self.due_to.isoformat()[:10] if self.due_to else None
        return data_formatted
