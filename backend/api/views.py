from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django_filters import rest_framework as filters

from api.serializers import (AssetSerializer, AssetInWorkSerializerGet,
                             AssetInWorkSerializerPost)
from assets.models import Asset, AssetInWork
from api.filters import AssetFilter, AssetInWorkFilter
from api.pagination import AssetPagination

User = get_user_model()


class AssetViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Asset."""
    http_method_names = ('get', 'post', 'patch', 'delete')
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AssetFilter
    pagination_class = AssetPagination

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = (AllowAny,)
        return super().get_permissions()


class AssetInWorkViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели AssetInWork."""
    http_method_names = ('get', 'post', 'patch', 'delete')
    queryset = AssetInWork.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AssetInWorkFilter
    pagination_class = AssetPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return AssetInWorkSerializerGet
        return AssetInWorkSerializerPost
