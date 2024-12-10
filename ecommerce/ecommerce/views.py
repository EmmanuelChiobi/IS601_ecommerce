from django.shortcuts import redirect, render
from products.models import Product
from cart.models import CartItem
from authapp.models import User
from django.db.models import F, Sum

def index(request):
  return redirect('/products')

def thankyou(request):
  if request.method == 'POST':
    cart = CartItem.objects.filter(user__userName = 'kris')
    print(cart)
    if cart:
      total_price = cart.aggregate(total=Sum(F('product__Price') * F('quantity')))['total']
      total_price = 0 if total_price == None else round(total_price)
      return render(request,'thankyou.html', context={'cart' : cart, 'total_price': total_price})
  else:
    return redirect('/products')
