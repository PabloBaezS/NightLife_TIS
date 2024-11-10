from django import template

register = template.Library()

@register.filter
def multiply(price, quantity):
    """Multiplies ticket price by quantity."""
    return price * quantity
