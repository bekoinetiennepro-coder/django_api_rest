from django.urls import path, include
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/products', ProductViewSet, basename='product')

urlpatterns = router.urls