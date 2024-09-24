import uuid
from django.db import models
from django.contrib.auth.models import User

class NightClub(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='nightclub_images/')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('normal', 'cover'),
        ('vip', 'VIP'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    nightclub = models.ForeignKey(NightClub, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='ticket_images/')

    def __str__(self):
        return f"{self.name} - {self.category}"

class CartItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticket.name} - {self.quantity}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tickets = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)
