from django.urls import include, path
from rest_framework import routers

# from api.views import

app_name = 'api'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
