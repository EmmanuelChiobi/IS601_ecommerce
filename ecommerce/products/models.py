from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=200)
    PID = models.IntegerField()
    Image = models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Specifications = models.TextField(max_length=500)
    Price = models.FloatField()
    StockAmount = models.IntegerField()
    
    
class Customer(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    cart = models.ManyToManyField(Product)