from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from tickets.forms import NightClubForm, TicketForm
from tickets.forms import TicketForm
from django.shortcuts import render, get_object_or_404, redirect
from tickets.models import Ticket, NightClub
from .forms import TicketForm
from django.contrib.admin.views.decorators import staff_member_required


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        id_type = request.POST['id_type']
        id_number = request.POST['id_number']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})

        # Create the user using the email as the username
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
            UserProfile.objects.create(user=user, id_number=id_number, id_type=id_type)
            return redirect('login')  # Redirect to login page after successful registration
        except Exception as e:
            return render(request, 'users/register.html', {'error': str(e)})

    return render(request, 'users/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html',
                          {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

# Admin dashboard view
@staff_member_required
def admin_dashboard(request):
    nightclubs = NightClub.objects.all()
    return render(request, 'users/admin_dashboard.html', {'nightclubs': nightclubs})

# Create nightclub view
@staff_member_required
def create_nightclub(request):
    if request.method == 'POST':
        form = NightClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = NightClubForm()
    return render(request, 'users/create_nightclub.html', {'form': form})

# Edit nightclub view
@staff_member_required
def edit_nightclub(request, pk):
    nightclub = get_object_or_404(NightClub, pk=pk)
    if request.method == 'POST':
        form = NightClubForm(request.POST, request.FILES, instance=nightclub)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = NightClubForm(instance=nightclub)
    return render(request, 'users/edit_nightclub.html', {'form': form, 'nightclub': nightclub})

# Delete nightclub view
@staff_member_required
def delete_nightclub(request, pk):
    nightclub = get_object_or_404(NightClub, pk=pk)
    if request.method == 'POST':
        nightclub.delete()
        return redirect('admin-dashboard')
    return render(request, 'users/delete_nightclub.html', {'nightclub': nightclub})



@staff_member_required
def nightclub_detail(request, pk):
    nightclub = get_object_or_404(NightClub, pk=pk)

    # Handle ticket creation
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.nightclub = nightclub  # Assign the nightclub to the ticket
            ticket.save()
            return redirect('nightclub-detail', pk=nightclub.pk)  # Redirect to the same page after ticket creation
    else:
        form = TicketForm()

    # Only fetch tickets that belong to this nightclub
    tickets = Ticket.objects.filter(nightclub=nightclub)

    return render(request, 'users/nightclub_detail.html', {
        'nightclub': nightclub,
        'tickets': tickets,
        'form': form,
    })
