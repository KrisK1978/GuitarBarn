from django.shortcuts import render
from .models import Product


# All products view.
def all_products(request):
    """ A view to show all products page with sorting and search enquiries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
