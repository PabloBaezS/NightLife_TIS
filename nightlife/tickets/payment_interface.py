# payment_interface.py

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, user, order, amount, **kwargs):
        """Procesa un pago específico para el usuario con la cantidad dada."""
        pass
