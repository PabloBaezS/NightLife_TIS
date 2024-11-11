from django import forms
from tickets.models import NightClub, Ticket

class NightClubForm(forms.ModelForm):
    class Meta:
        model = NightClub
        fields = ['name', 'address', 'description', 'image', 'latitude', 'longitude']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'description']
