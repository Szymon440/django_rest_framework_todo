from django.utils.translation import gettext_lazy as _
from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'TD', _('Todo')
    IN_PROGRESS = 'IP', _('In Progress')
    DONE = 'DN', _('Done')
