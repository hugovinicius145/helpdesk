from rest_framework.serializers import ModelSerializer
from locations.models import TbLocation

class LocationSerializer(ModelSerializer):
    class Meta:
        model = TbLocation
        fields = ("id","name_location","initials","desc_location")