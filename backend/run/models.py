from django.db import models
from django.contrib.auth.models import User
from activity.models import Activity


class Run(Activity):
    distance_km = models.DecimalField(max_digits=5, decimal_places=3)
    average_pace = models.DurationField()
    average_heart_rate = models.IntegerField(null=True, blank=True)
    elevation_gain = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    weather_conditions = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.person}'s run on {self.date}"

    @property
    def pace_per_km(self):
        """Calculate pace per kilometer."""
        if self.distance_km and self.duration:
            total_seconds = self.duration.total_seconds()
            pace_seconds_per_km = total_seconds / float(self.distance_km)
            return pace_seconds_per_km
        return None
