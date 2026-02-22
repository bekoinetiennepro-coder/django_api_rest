from api.models import Product
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.api.serializers import ProductSerializer1, ProductSerializer2
from rest_framework.decorators import action

class ProductViewSet(ModelViewSet):
    
    serializer_class = ProductSerializer1
    queryset= Product.objects.all()
    
    
    #route des produit superieur a 100
    
    @action(detail=False, methods=['GET'], url_path='expensive-products', url_name='expensive_products')
    def expensive_products(self, request, *args, **kwargs):
        products = Product.objects.filter(price__gt=1000)
        context= {
            "request": request,
        }
        serializer =ProductSerializer1 (products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)