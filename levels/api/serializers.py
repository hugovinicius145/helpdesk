from rest_framework.serializers import ModelSerializer
from levels.models import TbLevel

class LevelSerializer(ModelSerializer):
    class Meta:
        model = TbLevel
        fields = ("id","name_level","desc_level")