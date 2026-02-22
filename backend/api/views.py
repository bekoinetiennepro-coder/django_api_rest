from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

@csrf_exempt
def home(request):
    headers = request.headers
    params = request.GET.get("q")
    if request.method == "POST":
       
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data["name"],
            description=data["description"],
            price=data["price"]
        )
        data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
            "created_at": product.created_at,
            "update_at": product.update_at
        }
    print("------------------------------")
    print(data)
    return JsonResponse(data)