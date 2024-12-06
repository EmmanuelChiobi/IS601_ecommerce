from django.db import models
# from products.models import Product

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # cart = models.ManyToManyField(Product)