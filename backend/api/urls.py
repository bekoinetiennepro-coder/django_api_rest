from django.urls import path, include
from . import views
from api.api.api import product_api_view
from api.api.mixins import ProductListApiView, ProductCreateApiView, ProductDetailApiView, ProductUpdateApiView, ProductDeleteApiView, CombineApiViewSet

app_name = "api"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", product_api_view, name="product_api_view"),
    path("products/<int:pk>/", product_api_view, name="product_api_view_detail"),
    path("", include("api.routers")),
    path("v2/products-list/", ProductListApiView.as_view(), name="product_list_api_view"),
    path("v2/products-create/", ProductCreateApiView.as_view(), name="product_create_api_view"),
    path("v2/products-detail/<int:pk>/", ProductDetailApiView.as_view(), name="product_detail_api_view"),
    path("v2/products-update/<int:pk>/", ProductUpdateApiView.as_view(), name="product_update_api_view"),
    path("v2/products-delete/<int:pk>/", ProductDeleteApiView.as_view(), name="product_delete_api_view"),
    path("v3/products-combine/", CombineApiViewSet.as_view(), name="product_combine_api_view"),
    path("v3/products-combine/<int:pk>/", CombineApiViewSet.as_view(), name="product_combine_api_view_detail"),
    
    
]
