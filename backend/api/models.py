from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def get_price_in_erros(self):
        return f"{self.price} €"
    
    def get_description_short(self):
        return f"{self.name} - {self.price} €"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("api:product_api_view_detail", kwargs={"pk": self.pk})
    