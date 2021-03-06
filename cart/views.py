""" Views for Cart app """
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart based on quantity """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}!')
    else:
        cart[item_id] = quantity
        messages.success(
            request, f'Great, You added {product.name} to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def alter_cart(request, item_id):
    """ Alter the quantity of the chosen product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}!')
    else:
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from  shopping cart!')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the product from the shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = None
        cart = request.session.get('cart', {})

        if quantity:
            if not cart[item_id]:
                cart.pop(item_id)
        else:
            cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from  shopping cart!')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
