from django.db import models
from django.contrib.auth.models import User


class Run(models.Model):
    runner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='runs')
    date = models.DateField()
    start_time = models.TimeField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=3)
    duration = models.DurationField()
    average_pace = models.DurationField()
    average_heart_rate = models.IntegerField(null=True, blank=True)
    elevation_gain = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    weather_conditions = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.runner}'s run on {self.date}"

    @property
    def pace_per_km(self):
        """Calculate pace per kilometer."""
        if self.distance_km and self.duration:
            total_seconds = self.duration.total_seconds()
            pace_seconds_per_km = total_seconds / float(self.distance_km)
            return pace_seconds_per_km
        return None
