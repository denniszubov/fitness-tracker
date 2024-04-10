from django.db import models
from django.contrib.auth.models import User
from activity.models import Activity


class Swim(Activity):
    UNIT_CHOICES = (
        ("m", "meters"),
        ("yd", "yards"),
    )
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name='swims')
    distance = models.DecimalField(max_digits=8, decimal_places=3)
    distance_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default="m")   
    average_heart_rate = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.person}'s swim on {self.date}"