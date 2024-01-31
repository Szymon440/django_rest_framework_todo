from django.db import models
from .choices import TaskStatus


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )
    updated_at = models.DateTimeField(auto_now=True)
