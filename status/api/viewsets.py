from rest_framework.viewsets import ModelViewSet
from status.models import TbStatus
from .serializers import StatusSerializer

class StatusViewSet(ModelViewSet):
    queryset = TbStatus.objects.all()
    serializer_class = StatusSerializer