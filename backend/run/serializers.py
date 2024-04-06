from rest_framework import serializers
from .models import Run
from activity.serializers import ActivitySerializer

class RunSerializer(ActivitySerializer):
    class Meta(ActivitySerializer.Meta):
        model = Run
        fields = '__all__'
