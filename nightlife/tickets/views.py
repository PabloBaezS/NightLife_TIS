from .models import Ticket, CartItem, Order, Payment
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NightClubForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, NightClub
from .forms import TicketForm
from users.models import UserProfile
from rest_framework import viewsets
from .models import NightClub
from .serializers import NightClubSerializer
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import NightClub
from .serializers import NightClubSerializer
from django.contrib.auth.decorators import login_required
from .models import CartItem


def TicketListView(request, nightclub_id):
    try:
        nightclub = get_object_or_404(NightClub, pk=nightclub_id)  # Obtiene la discoteca actual
        tickets = Ticket.objects.filter(nightclub=nightclub)  # Filtra los tickets para esa discoteca
    except NightClub.DoesNotExist:
        return HttpResponse("NightClub no encontrado.", status=404)

    return render(request, 'tickets/ticket_list.html', {
        'nightclub': nightclub,
        'tickets': tickets,
    })


def TicketDetailView(request, pk):
    # Obtiene el ticket usando el ID del ticket
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        # Agregar ticket al carrito
        quantity = int(request.POST.get('quantity',
                                        1))  # Por defecto, añade 1 si no se proporciona cantidad
        CartItem.objects.create(ticket=ticket, user=request.user,
                                quantity=quantity)
        return redirect('cart')  # Redirige a la página del carrito

    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})



@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum([item.ticket.price * item.quantity for item in cart_items])

    return render(request, 'tickets/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def order_confirmation(request):
    cart_items = CartItem.objects.filter(user=request.user)
    #order = Order.objects.create(user=request.user)
    #order.tickets.set(cart_items)
    #order.save()
    return render(request, 'tickets/order_confirmation.html')


def home_view(request):
    nightclubs = NightClub.objects.all()
    # print("Nightclub IDs:", [nightclub.id for nightclub in nightclubs])  # debug
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



@staff_member_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    nightclub_id = ticket.nightclub.pk  # Save the nightclub ID before deletion
    ticket.delete()
    return redirect('nightclub-detail', pk=nightclub_id)  # Redirect to the same nightclub's detail page


def add_ticket(request, nightclub_id):
    nightclub = get_object_or_404(NightClub, pk=nightclub_id)  # Get the specific nightclub

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.nightclub = nightclub  # Assign the nightclub to the ticket
            ticket.save()
            return redirect('nightclub-detail', pk=nightclub_id)  # Redirect back to nightclub detail
    else:
        form = TicketForm()

    return render(request, 'tickets/add_ticket.html', {'form': form, 'nightclub': nightclub})


from django.shortcuts import render, redirect
from .models import Order

def payment_view(request):
    if request.method == "POST":
        # Retrieve all cart items for the current user
        cart_items = CartItem.objects.filter(user=request.user)

        # Calculate the total price
        #total_price = sum([item.ticket.price * item.quantity for item in cart_items])

        # Create the order
        #order = Order.objects.create(user=request.user)


        # Optionally, clear the cart after creating the order
        #cart_items.delete()

        # Redirect to the order confirmation page
        return redirect('order-confirmation')

    return render(request, 'tickets/payment.html')

def payment_success_view(request):
    return render(request, 'payment_success.html')


from django.shortcuts import redirect, get_object_or_404
from .models import CartItem
from tickets.models import Ticket

def add_to_cart(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = request.user

    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        # Get or create the cart item for this user and ticket
        cart_item, created = CartItem.objects.get_or_create(user=user, ticket=ticket)
        cart_item.quantity = quantity  # Update quantity
        cart_item.save()  # Save the updated cart item

        return redirect('cart')

@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


class NightClubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Un ViewSet para ver una lista de discotecas o detalles de una en particular.
    """
    queryset = NightClub.objects.all()
    serializer_class = NightClubSerializer


def download_nightclub_json(request, pk):
    # Obtén el club nocturno específico
    nightclub = get_object_or_404(NightClub, pk=pk)

    # Serializa los datos del club nocturno
    serializer = NightClubSerializer(nightclub)
    data = serializer.data

    # Crea la respuesta en formato JSON
    response = HttpResponse(
        json.dumps(data, indent=4),
        # Convierte a JSON con indentación para mejorar la visualización
        content_type='application/json'
    )

    # Configura el encabezado para forzar la descarga con un nombre de archivo
    response[
        'Content-Disposition'] = f'attachment; filename="{nightclub.name}_details.json"'
    return response

