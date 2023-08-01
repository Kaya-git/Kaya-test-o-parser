from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('products', ProductViewSet)

urlpatterns = v1_router.urls
