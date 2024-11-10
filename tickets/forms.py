from django import forms
from .models import NightClub, Ticket
from django import forms
from .models import Ticket


class NightClubForm(forms.ModelForm):
    class Meta:
        model = NightClub
        fields = ['name', 'address', 'description', 'image']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'description']  # Show ticket type, price, and description
