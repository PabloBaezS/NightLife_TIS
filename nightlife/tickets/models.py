import uuid
from django.contrib.auth.models import User
from django.db import models

class NightClub(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)  # Allow null and blank values
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='nightclubs/', blank=True, null=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    TICKET_CHOICES = [
        ('normal', 'Normal Cover'),
        ('vip', 'VIP Cover'),
    ]
    nightclub = models.ForeignKey(NightClub, related_name='tickets', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=TICKET_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ticket_type} - {self.nightclub.name}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.ticket.get_ticket_type_display()}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Make sure this is a ForeignKey
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"