""" URLs Patterns for Cart app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('alter/<item_id>/', views.alter_cart, name='alter_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
