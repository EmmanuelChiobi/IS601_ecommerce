from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from products.models import Product
from products.models import Customer
from .models import CartItem
from django.views.decorators.csrf import csrf_protect
from django.db.models import F, Sum

def cart(request, user="kris"):
    user = Customer.objects.filter(userName=user)
    userCart = CartItem.objects.filter(user_id=user[0].id)
    total_price = userCart.aggregate(total=Sum(F('product__Price') * F('quantity')))['total']
    return render(request, 'cart.html', context = {"products": userCart, 'total_price': total_price })

def cart_add(request, id, user="kris"):
    referer = request.META.get('HTTP_REFERER', 'unknown').split('/')[-2]
    user = Customer.objects.filter(userName=user)
    product = Product.objects.filter(id = id)
    userCart = CartItem.objects.filter(user_id=user[0].id) 
    if userCart.count() == 0:
        CartItem.objects.create(user=user[0], quantity=1, product=product[0]).save()

    else:
        if userCart.filter(product_id=id).count() == 0:
            CartItem.objects.create(user=user[0], quantity=1, product=product[0]).save()
        else:
            userCart.filter(product_id=product[0].id).update(quantity=F('quantity')+1)
    if referer == 'products':
        return redirect('/products')
    elif referer == 'cart':
        return redirect('/cart')

def cart_delete(request, id, user="kris"):
    referer = request.META.get('HTTP_REFERER', 'unknown').split('/')[-2]
    user = Customer.objects.filter(userName=user)
    product = Product.objects.filter(id = id)
    userCart = CartItem.objects.filter(user_id=user[0].id)
    curProduct = userCart.filter(product_id = id)
    if userCart.filter(product_id=product[0].id)[0].quantity == 1:
        CartItem.objects.filter(user_id = user[0].id).filter(product_id=product[0].id).delete()
    else:
        CartItem.objects.filter(user_id = user[0].id).filter(product_id=product[0].id).update(quantity=F('quantity')-1)
        
    if referer == 'products':
        return redirect('/products')
    elif referer == 'cart':
        return redirect('/cart')