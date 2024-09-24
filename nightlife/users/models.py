from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=100)
    id_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username