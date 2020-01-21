from rest_framework.serializers import ModelSerializer
from usersadmin.models import TbUseradmin

class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = TbUseradmin
        fields = ("id","userdomainname","pass_field")