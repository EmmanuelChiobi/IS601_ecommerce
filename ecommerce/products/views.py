from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
  if request.method == "POST":
    sort = request.POST.get("sort")
    print(sort)
    if sort == "ASC":
      products = Product.objects.all().order_by('Price')
    else:
      products = Product.objects.all().order_by('-Price')
  else:
    products = Product.objects.all()  
  
  return render(request, 'products.html', context={'products' : products})

def product(request, id):
  product = Product.objects.filter(id = id)
  return render(request, 'product.html', context={'product' : product})

@csrf_protect
def search(request):
  key = request.POST["key"]
  print(key)
  product = Product.objects.filter(Name__icontains=key)
  return render(request, 'product.html', context={'product' : product})