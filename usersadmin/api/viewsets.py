from rest_framework.viewsets import ModelViewSet
from usersadmin.models import TbUseradmin
from .serializers import UserAdminSerializer

class UserAdminViewSet(ModelViewSet):
    queryset = TbUseradmin.objects.all()
    serializer_class = UserAdminSerializer