# tickets/templatetags/cart_extras.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0  # Retorna 0 en caso de error para evitar problemas en la plantilla
