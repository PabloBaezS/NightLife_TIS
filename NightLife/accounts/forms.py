from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Custom Signup Form extending the UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    phoneNumber = forms.CharField(max_length=15, required=False, help_text="Optional. Enter your phone number.")
    photo = forms.ImageField(required=False, help_text="Optional. Upload a profile picture.")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phoneNumber', 'photo', 'password1', 'password2')

# Authentication Form (Optional) - You can just use the default AuthenticationForm from Django
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
