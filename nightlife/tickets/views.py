from .models import Ticket, CartItem, Order
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import NightClub, Ticket
from .forms import NightClubForm, TicketForm
from .models import Ticket


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


@staff_member_required
def create_nightclub_view(request):
    if request.method == 'POST':
        form = NightClubForm(request.POST, request.FILES)
        ticket_formset = TicketForm(request.POST)

        if form.is_valid() and ticket_formset.is_valid():
            nightclub = form.save()

            # Save ticket information
            for form in ticket_formset:
                ticket = form.save(commit=False)
                ticket.nightclub = nightclub
                ticket.save()

            return redirect('admin-dashboard')  # Redirect to the admin dashboard
    else:
        form = NightClubForm()
        ticket_formset = TicketForm()

    return render(request, 'admin/create_nightclub.html', {
        'form': form,
        'ticket_formset': ticket_formset
    })


def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    nightclub = ticket.nightclub  # Save the related nightclub before deleting
    ticket.delete()
    return redirect('nightclub-detail', pk=nightclub.pk)  # Redirect to the same nightclub detail page

