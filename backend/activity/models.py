from django.db import models


class Activity(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    general_notes = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
