from django.urls import path
from . import views
from api.api.api import product_api_view


urlpatterns = [
    path("", views.home, name="home"),
    path("products/", product_api_view, name="product_api_view"),
    path("products/<int:pk>/", product_api_view, name="product_api_view_with_pk"),
    
]
