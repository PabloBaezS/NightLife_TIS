from django import forms
from .models import NightClub, Ticket

class NightClubForm(forms.ModelForm):
    class Meta:
        model = NightClub
        fields = ['name', 'address', 'description', 'image']  # Adjust fields as needed

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'description']
