""" Views for Checkout app """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, "Oops, there is nothing in your cart at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IFitMDiIycHjvUXg0qdvImDMJEsZ1yf3sFVczeAXLEDnnnUAwnYLI30cAyJPLN6ZynbmDXJWO25PzJQ0Kt9LEhq00C4r3ysnv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
