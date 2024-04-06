from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name='does')
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    general_notes = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
