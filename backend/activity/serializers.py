from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["person", "date", "start_time", "duration", "general_notes"]
        abstract = True
