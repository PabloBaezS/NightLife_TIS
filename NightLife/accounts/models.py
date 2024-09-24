from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model extending Django's AbstractUser
class CustomUser(AbstractUser):
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)  # Optional phone number field
    photo = models.ImageField(upload_to='users/', null=True, blank=True)  # Optional profile picture

    def __str__(self):
        return self.username
