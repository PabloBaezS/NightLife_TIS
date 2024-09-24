from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

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
