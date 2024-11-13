from django.conf import settings
from django.utils.translation import gettext as _  # Para usar traducción en Python
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets
from .models import Ticket, NightClub, CartItem, Order, Payment
from .forms import NightClubForm, TicketForm
from .serializers import NightClubSerializer
from django.http import FileResponse
from .utils import generate_pdf_receipt
from .payment_processors import CreditCardPaymentProcessor, AccountBalancePaymentProcessor
from django.utils import translation
import json
from django.shortcuts import redirect


def set_language_in_view(request):
    if request.method == 'POST':
        language = request.POST.get('language', 'en')  # Idioma predeterminado: inglés
        # Activa el idioma seleccionado
        translation.activate(language)
        # Almacena el idioma en la sesión
        request.session['django_language'] = language
        # Almacena el idioma en la cookie
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        response.set_cookie('django_language', language)
        return response



def TicketListView(request, nightclub_id):
    set_language_in_view(request)  # Activa idioma según sesión
    nightclub = get_object_or_404(NightClub, pk=nightclub_id)
    tickets = Ticket.objects.filter(nightclub=nightclub)
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY

    return render(request, 'tickets/ticket_list.html', {
        'nightclub': nightclub,
        'tickets': tickets,
        'google_maps_api_key': google_maps_api_key,
    })


@login_required(login_url='login')
def TicketDetailView(request, pk):
    set_language_in_view(request)  # Activa idioma según sesión
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        CartItem.objects.create(ticket=ticket, user=request.user, quantity=quantity)
        return redirect('cart')

    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


@login_required
def cart_view(request):
    set_language_in_view(request)  # Activa idioma según sesión
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum([item.ticket.price * item.quantity for item in cart_items])

    return render(request, 'tickets/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'tickets/order_confirmation.html', {'order': order})


def home_view(request):
    set_language_in_view(request)  # Activa idioma según sesión
    search_query = request.GET.get('search', '')

    if search_query:
        nightclubs = NightClub.objects.filter(name__icontains=search_query)
    else:
        nightclubs = NightClub.objects.all()

    return render(request, 'tickets/home.html', {
        'nightclubs': nightclubs,
        'search_query': search_query,
    })

@staff_member_required
def create_nightclub_view(request):
    set_language_in_view(request)  # Activa idioma según sesión
    if request.method == 'POST':
        form = NightClubForm(request.POST, request.FILES)
        ticket_formset = TicketForm(request.POST)

        if form.is_valid() and ticket_formset.is_valid():
            nightclub = form.save()

            for form in ticket_formset:
                ticket = form.save(commit=False)
                ticket.nightclub = nightclub
                ticket.save()

            return redirect('admin-dashboard')
    else:
        form = NightClubForm()
        ticket_formset = TicketForm()

    return render(request, 'admin/create_nightclub.html', {
        'form': form,
        'ticket_formset': ticket_formset
    })


@staff_member_required
def delete_ticket(request, pk):
    set_language_in_view(request)  # Activa idioma según sesión
    ticket = get_object_or_404(Ticket, pk=pk)
    nightclub_id = ticket.nightclub.pk
    ticket.delete()
    return redirect('nightclub-detail', pk=nightclub_id)


def add_ticket(request, nightclub_id):
    set_language_in_view(request)  # Activa idioma según sesión
    nightclub = get_object_or_404(NightClub, pk=nightclub_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.nightclub = nightclub
            ticket.save()
            return redirect('nightclub-detail', pk=nightclub_id)
    else:
        form = TicketForm()

    return render(request, 'tickets/add_ticket.html', {'form': form, 'nightclub': nightclub})


def payment_view(request):
    set_language_in_view(request)
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.ticket.price * item.quantity for item in cart_items)

    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=total_price)
        payment_method = request.POST.get('payment_method')

        if payment_method == 'credit_card':
            processor = CreditCardPaymentProcessor()
            processor.process_payment(request.user, order, total_price, card_number=request.POST.get('card_number'))
        elif payment_method == 'account_balance':
            processor = AccountBalancePaymentProcessor()
            processor.process_payment(request.user, order, total_price)

        cart_items.delete()
        # Redirect with the order ID as a parameter
        return redirect('order-confirmation', order_id=order.id)

    return render(request, 'tickets/payment.html', {'total_price': total_price})


def payment_success_view(request):
    set_language_in_view(request)  # Activar idioma según sesión
    return render(request, 'payment_success.html')


@login_required
def add_to_cart(request, ticket_id):
    set_language_in_view(request)  # Activa idioma según sesión
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = request.user

    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(user=user, ticket=ticket)
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart')


@login_required
def remove_cart_item(request, item_id):
    set_language_in_view(request)  # Activa idioma según sesión
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


class NightClubViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NightClub.objects.all()
    serializer_class = NightClubSerializer


def download_nightclub_json(request, pk):
    set_language_in_view(request)  # Activa idioma según sesión
    nightclub = get_object_or_404(NightClub, pk=pk)
    serializer = NightClubSerializer(nightclub)
    data = serializer.data

    response = HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
    response['Content-Disposition'] = f'attachment; filename="{nightclub.name}_details.json"'
    return response

# tickets/views.py


def download_receipt(request, order_id):
    buffer = generate_pdf_receipt(order_id)
    return FileResponse(buffer, as_attachment=True, filename=f"Receipt_Order_{order_id}.pdf")


from django.shortcuts import HttpResponse
from django.utils.translation import gettext as _
from django.utils import translation
from django.utils.translation import get_language


def test_translation_view(request):
    translation.activate('es')
    text = _("NightLife - Explore Nightclubs")
    return HttpResponse(text)

def debug_language_view(request):
    current_language = get_language()
    return HttpResponse(f"Current Language: {current_language}")