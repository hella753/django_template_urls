from django.db.models import Sum
from django.shortcuts import render
from order.models import Cart
from order.models import CartItems


# Create your views here.
def cart(request):
    cartitems = CartItems.objects.filter(cart__user__username="customer").select_related("product").all()
    cart = Cart.objects.get(user__username="customer")
    subtotal = cartitems.aggregate(total=Sum("total_price")).get("total")
    total = subtotal + cart.flat_rate
    context={
        "cartitems": cartitems,
        "subtotal": subtotal,
        "total": total,
        "cart": cart
    }

    return render(request, "cart/cart.html", context)


def checkout(request):
    cartitems = CartItems.objects.filter(cart__user__username="customer").select_related("product").all()
    cart = Cart.objects.get(user__username="customer")
    subtotal = cartitems.aggregate(total=Sum("total_price")).get("total")
    total = subtotal + cart.flat_rate
    context={
        "cartitems": cartitems,
        "total": total,
        "subtotal": subtotal,
        "cart": cart
    }
    return render(request, "checkout/chackout.html", context)