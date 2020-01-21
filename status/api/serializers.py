from rest_framework.serializers import ModelSerializer
from status.models import TbStatus

class StatusSerializer(ModelSerializer):
    class Meta:
        model = TbStatus
        fields = ("id","name_status","description")