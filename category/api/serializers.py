from rest_framework.serializers import ModelSerializer
from category.models import TbCategory

class CategorySerializer(ModelSerializer):
    class Meta:
        model = TbCategory
        fields = ("id","name_category","desc_category")