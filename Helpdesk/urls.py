from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from category.api.viewsets import CategoryViewSet
from levels.api.viewsets import LevelViewSet
from locations.api.viewsets import LocationViewSet
from status.api.viewsets import StatusViewSet
from tbtypes.api.viewsets import TypeViewSet
from commentarys.api.viewsets import CommentaryViewSet
from usersadmin.api.viewsets import UserAdminViewSet


router = routers.DefaultRouter()
router.register(r'categorys', CategoryViewSet, basename='Category')
router.register(r'levels', LevelViewSet, basename='Levels')
router.register(r'locations', LocationViewSet, basename='Locations')
router.register(r'status', StatusViewSet, basename='Status')
router.register(r'types',TypeViewSet, basename='TbTypes') 
router.register(r'commentarys', CommentaryViewSet, basename='Commentarys')
router.register(r'usersadmin', UserAdminViewSet, basename='UsersAdmin')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
