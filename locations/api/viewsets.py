from rest_framework.viewsets import ModelViewSet
from locations.models import TbLocation
from .serializers import LocationSerializer

class LocationViewSet(ModelViewSet):
    queryset = TbLocation.objects.all()
    serializer_class = LocationSerializer