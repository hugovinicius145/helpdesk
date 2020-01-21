from rest_framework.viewsets import ModelViewSet
from tbtypes.models import TbType
from .serializers import TypeSerializer

class TypeViewSet(ModelViewSet):
    queryset = TbType.objects.all()
    serializer_class = TypeSerializer