from .models import Swim
from activity.serializers import ActivitySerializer

class SwimSerializer(ActivitySerializer):
    class Meta(ActivitySerializer.Meta):
        model = Swim
        fields = '__all__'
