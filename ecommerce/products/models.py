from django.db import models

# Model for products in the catalog
class Product(models.Model):
    Name = models.CharField(max_length=200)
    PID = models.IntegerField()
    Image = models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Specifications = models.TextField(max_length=500)
    Description = models.TextField(max_length=500)
    Price = models.FloatField()
    StockAmount = models.IntegerField()
    
# Model for users
class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
