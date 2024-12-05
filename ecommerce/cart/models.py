from django.db import models
from products.models import Product, Customer
# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)