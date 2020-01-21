from rest_framework.viewsets import ModelViewSet
from imgs.models import TbUseradmin
from .serializers import UserAdminSerializer

class UserAdminViewSet(ModelViewSet):
    queryset = TbUseradmin.objects.all()
    serializer_class = UserAdminSerializer