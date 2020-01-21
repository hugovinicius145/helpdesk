from rest_framework.viewsets import ModelViewSet
from commentarys.models import TbCommentary
from .serializers import CommentarySerializer

class CommentaryViewSet(ModelViewSet):
    queryset = TbCommentary.objects.all()
    serializer_class = CommentarySerializer