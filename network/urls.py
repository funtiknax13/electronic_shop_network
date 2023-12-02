from django.urls import path
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import ProductViewSet, CompanyViewSet

app_name = NetworkConfig.name


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'companies', CompanyViewSet, basename='companies')


urlpatterns = [
] + router.urls
