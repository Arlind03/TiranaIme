from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Parking
from .Serializers import ParkingSerializer

class ParkingListView(APIView):
    def get(self, request):
        parkings = Parking.objects.all().prefetch_related('parking_spaces')
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)
