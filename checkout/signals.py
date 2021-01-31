""" Signals for Checkout app """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


"""
This decorator executes the function any time
the signal is sent
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    This updates order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    This updates order total on lineitem delete
    """
    instance.order.update_total
