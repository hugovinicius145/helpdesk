from rest_framework.viewsets import ModelViewSet
from levels.models import TbLevel
from .serializers import LevelSerializer

class LevelViewSet(ModelViewSet):
    queryset = TbLevel.objects.all()
    serializer_class = LevelSerializer