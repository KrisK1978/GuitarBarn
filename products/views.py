from django.shortcuts import render, get_object_or_404
from .models import Product


# All products view.
def all_products(request):
    """ A view to show all products page with sorting and search enquiries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# Product details view.
def product_detail(request, product_id):
    """ A view to display product details  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
