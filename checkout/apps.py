""" Apps for Checkout app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    """
    This imports signals module
    """
    def ready(self):
        import checkout.signals
