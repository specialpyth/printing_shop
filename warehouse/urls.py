from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]