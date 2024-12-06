from cart.models import CartItem
from django.db.models import Sum

def cart_total(request):
    item_count = CartItem.objects.aggregate(Sum('quantity'))['quantity__sum']
    if item_count == None:
        item_count = 0
    return {"item_count": item_count}