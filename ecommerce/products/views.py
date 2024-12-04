from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from .models import Customer
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
  """
  View for the homepage of the site.
  CSRF Protection to secure the POST Data.

  Args:
      request: Incoming Request Data.
  Returns:
      render: Response for the incoming request along with all the products.
  """
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
  """
  View for the product site.

  Args:
      request: Incoming Request Data.
      pid: Product ID of the Product that was selected.
      
  Returns:
      render: Response for the incoming request along with the product data.
  """
  product = Product.objects.filter(PID = pid)
  return render(request, 'product.html', context={'product' : product})

@csrf_protect
def search(request):
  """
  View for the search page.
  CSRF Protection to secure the POST Data.

  Args:
      request: Incoming Request Data.
  Returns:
      render: Response for the incoming request along with the products macthing the search criteria.
  """
  
  key = request.POST["key"]
  product = Product.objects.filter(Name__icontains=key)
  return render(request, 'product.html', context={'product' : product})

def cart(request, user="U1"):
  user = Customer.objects.filter(userName=user)
  products = user[0].cart.all()
  return render(request, 'cart.html', context = {"products": products })
  