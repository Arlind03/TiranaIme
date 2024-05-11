from rest_framework import serializers
from .models import Parking, ParkingSpace

class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = ['id', 'parking_space_status']

class ParkingSerializer(serializers.ModelSerializer):
    parking_spaces = ParkingSpaceSerializer(many=True, read_only=True, source='parking_spaces')

    class Meta:
        model = Parking
        fields = ['id', 'parking_name', 'street_name', 'total_spaces', 'lon', 'lat', 'parking_spaces']
