from rest_framework.serializers import ModelSerializer
from imgs.models import TbImg

class ImgSerializer(ModelSerializer):
    class Meta:
        model = TbImg
        fields = ("id","ticket_id","img")