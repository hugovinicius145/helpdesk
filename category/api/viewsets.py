from rest_framework.viewsets import ModelViewSet
from category.models import TbCategory
from .serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = TbCategory.objects.all()
    serializer_class = CategorySerializer