from django.utils.translation import gettext_lazy as _

from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'TD', _('Todo')
    IN_PROGRESS = 'IP', _('In Progress')
    DONE = 'DN', _('Done')


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )
    updated_at = models.DateTimeField(auto_now=True)
