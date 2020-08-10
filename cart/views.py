from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    if (int(request.POST.get('quantity'))) == 0:
        return redirect(reverse('index'))
    else:
        quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    product = get_object_or_404(Product, pk=id)
    messages.success(request, 'You have successfuly added - "%s" x%s - to your shopping cart!' % (product.name, quantity))
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    product = get_object_or_404(Product, pk=id)
    messages.success(request, 'You have successfuly amended - "%s" - to quantity: %s - in your shopping cart!' % (product.name, quantity))
    return redirect(reverse('view_cart'))