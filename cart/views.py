from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """A view that display cart content page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add quantity of the specified product to the cart / prevents literal fo int() error"""
    quantity = int(request.POST.get('quantity') or 0)
    if quantity == 0:
        messages.warning(request, 'Please enter a quantity.')

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def update_cart(request, id):
    """Update the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
