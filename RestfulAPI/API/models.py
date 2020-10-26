from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
