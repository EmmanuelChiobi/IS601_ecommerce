from cart.models import CartItem
from django.db.models import Sum
from django.contrib.auth import get_user

def cart_total(request):
    item_count = CartItem.objects.filter(user = get_user(request).username).aggregate(Sum('quantity'))['quantity__sum']
    if item_count == None:
        item_count = 0
    return {"item_count": item_count}

def cur_user(request):
    print(get_user(request).username)
    return {"user" : get_user(request).username}