from django.urls import include, path
from rest_framework import routers

from api.views import AssetInWorkViewSet, AssetViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('assets', AssetViewSet, basename='asset')
router.register('assets_in_work', AssetInWorkViewSet, basename='asset_in_work')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
