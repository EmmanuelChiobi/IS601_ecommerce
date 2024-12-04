from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product

# Create your views here.
def home(request):
  products = Product.objects.all()
  return render(request, 'products.html', context={'products' : products})

def product(request, id):
  product = Product.objects.filter(id = id)
  return render(request, 'product.html', context={'product' : product})

def search(request, key):
  product = Product.objects.filter(name__icontains='pad')
  return render(request, 'product.html', context={'product' : product})