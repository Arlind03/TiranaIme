from django.urls import path
from .views import ParkingListView

urlpatterns = [
    path('api/parkings/', ParkingListView.as_view(), name='parking-list'),
]
