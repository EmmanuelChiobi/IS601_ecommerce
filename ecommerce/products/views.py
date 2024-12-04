from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from .models import Customer
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
  if request.method == "POST":
    sort = request.POST.get("sort")
    if sort == "ASC":
      products = Product.objects.all().order_by('Price')
    else:
      products = Product.objects.all().order_by('-Price')
  else:
    products = Product.objects.all()  
  
  return render(request, 'products.html', context={'products' : products})

def product(request, pid):
  product = Product.objects.filter(PID = pid)
  return render(request, 'product.html', context={'product' : product})

@csrf_protect
def search(request):
  key = request.POST["key"]
  product = Product.objects.filter(Name__icontains=key)
  return render(request, 'product.html', context={'product' : product})

def cart(request, user="U1"):
  user = Customer.objects.filter(userName=user)
  products = user[0].cart.all()
  return render(request, 'cart.html', context = {"products": products })
  