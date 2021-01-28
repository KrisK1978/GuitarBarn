# Import Product and Category models.
from django.contrib import admin
from .models import Product, Category

# Product and Category models.
admin.site.register(Product)
admin.site.register(Category)
