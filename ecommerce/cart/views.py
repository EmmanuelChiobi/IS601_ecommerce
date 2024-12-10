from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user
from products.models import Product
from .models import CartItem
from django.views.decorators.csrf import csrf_protect
from django.db.models import F, Sum

def cart(request):
    userCart = CartItem.objects.filter(user=get_user(request).username)
    total_price = userCart.aggregate(total=Sum(F('product__Price') * F('quantity')))['total']
    total_price = 0 if total_price == None else round(total_price)
    return render(request, 'cart.html', context = {"products": userCart, 'total_price': total_price })

def cart_add(request, id):
    url = request.META.get('HTTP_REFERER', 'unknown')
    referer = url.split('/')[-2]
    extension = url.split('/')[-1]
    product = Product.objects.filter(id = id)
    userCart = CartItem.objects.filter(user=get_user(request).username) 
    if userCart.count() == 0:
        CartItem.objects.create(user=get_user(request).username, quantity=1, product=product[0]).save()

    else:
        if userCart.filter(product_id=id).count() == 0:
            CartItem.objects.create(user=get_user(request).username, quantity=1, product=product[0]).save()
        else:
            userCart.filter(product_id=product[0].id).update(quantity=F('quantity')+1)
    if referer == 'products':
        if(extension == ' '):
            return redirect('/products')
        else:
            return redirect(url)
    elif referer == 'cart':
        return redirect('/cart')
    elif referer == 'product':
        return redirect(url)
    
    

def cart_delete(request, id):
    url = request.META.get('HTTP_REFERER', 'unknown')
    referer = url.split('/')[-2]
    extension = url.split('/')[-1]
    product = Product.objects.filter(id = id)
    userCart = CartItem.objects.filter(user=get_user(request).username)
    #curProduct = userCart.filter(product_id = id)
    if userCart.filter(product_id=product[0].id)[0].quantity == 1:
        CartItem.objects.filter(user = get_user(request).username).filter(product_id=product[0].id).delete()
    else:
        CartItem.objects.filter(user = get_user(request).username).filter(product_id=product[0].id).update(quantity=F('quantity')-1)
        
    if referer == 'products':
        if(extension == ' '):
            return redirect('/products')
        else:
            return redirect(url)
    elif referer == 'cart':
        return redirect('/cart')
    elif referer == 'product':
        return redirect(url)