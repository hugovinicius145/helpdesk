from rest_framework.serializers import ModelSerializer
from tbtypes.models import TbType

class TypeSerializer(ModelSerializer):
    class Meta:
        model = TbType
        fields = ("id","name_type","desc_type")