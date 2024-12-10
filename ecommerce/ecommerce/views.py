from django.shortcuts import redirect, render
from products.models import Product
from cart.models import CartItem
from django.db.models import F, Sum
from django.contrib.auth import get_user

def index(request):
  return redirect('/products')

def thankyou(request):
  if request.method == 'POST':
    cart = CartItem.objects.filter(user = get_user(request).username)
    print(cart)
    if cart:
      total_price = cart.aggregate(total=Sum(F('product__Price') * F('quantity')))['total']
      total_price = 0 if total_price == None else round(total_price)
      for x in cart:
        print(x.quantity)
        Product.objects.filter(id = x.product.id).update(StockAmount = x.product.StockAmount - x.quantity)
      cart.delete()
      return render(request,'thankyou.html', context={'cart' : cart, 'total_price': total_price})
  else:
    return redirect('/products')
