from django.urls import path, include
from api.api.viewset import ProductViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/products', ProductViewSet, basename='product')
router.register('v1/users', UserViewSet, basename='user')

urlpatterns = router.urls