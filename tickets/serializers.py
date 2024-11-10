from rest_framework import serializers
from .models import NightClub

class NightClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightClub
        fields = ('id', 'name', 'address', 'description', 'image', 'latitude', 'longitude')
