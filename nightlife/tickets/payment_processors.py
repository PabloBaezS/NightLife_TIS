# payment_processors.py

from .models import Payment, Order
from .payment_interface import PaymentProcessor

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, user, order, amount, **kwargs):
        # Simular lógica de pago con tarjeta de crédito
        card_number = kwargs.get("card_number")
        # Lógica de validación y procesamiento
        payment = Payment(order=order, amount=amount, payment_status='completed')
        payment.save()
        return payment

class AccountBalancePaymentProcessor(PaymentProcessor):
    def process_payment(self, user, order, amount, **kwargs):
        payment = Payment(order=order, amount=amount,
                          payment_status='completed')
        payment.save()
        return payment
