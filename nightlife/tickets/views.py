from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, CartItem, Order
from .models import NightClub


def TicketListView(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


def TicketDetailView(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        # Add ticket to cart
        quantity = int(request.POST['quantity'])
        CartItem.objects.create(ticket=ticket, user=request.user,
                                quantity=quantity)
        return redirect('cart')

    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'tickets/cart.html', {'cart_items': cart_items})


def order_confirmation(request):
    cart_items = CartItem.objects.filter(user=request.user)
    order = Order.objects.create(user=request.user)
    order.tickets.set(cart_items)
    order.save()
    return render(request, 'tickets/order_confirmation.html', {'order': order})


def home_view(request):
    nightclubs = NightClub.objects.all()
    return render(request, 'tickets/home.html', {'nightclubs': nightclubs})