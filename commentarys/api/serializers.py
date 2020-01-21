from rest_framework.serializers import ModelSerializer
from commentarys.models import TbCommentary

class CommentarySerializer(ModelSerializer):
    class Meta:
        model = TbCommentary
        fields = ("id","ticket_id","commentary","status_id")