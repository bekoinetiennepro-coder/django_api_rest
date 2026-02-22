from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer1, ProductSerializer2

#comment developper une api en django rest framework avec le decorateur api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])

def product_api_view(request, pk=None, *args, **kwargs):
    
    pk = pk
    context = {
        "request": request, 
       
    }
    if request.method == 'GET':
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer1(product, context=context)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        products = Product.objects.all()
        serializer = ProductSerializer1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    if request.method == 'POST':
        serializer = ProductSerializer1(data=request.data, context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    if request.method == 'PUT':
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductSerializer1(product, data=request.data, context=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Product ID is required for PUT request"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            
            product.delete()
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Product ID is required for DELETE request"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'PATCH':
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductSerializer1(product, data=request.data, partial=True, context=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Product ID is required for PATCH request"}, status=status.HTTP_400_BAD_REQUEST)