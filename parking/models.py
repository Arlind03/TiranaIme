from django.db import models

class Parking(models.Model):
    parking_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    total_spaces = models.IntegerField()
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.parking_name

class ParkingSpace(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='parking_spaces')
    parking_space_status = models.BooleanField()

    def __str__(self):
        return f"{self.parking.parking_name} - Space ID {self.id}: {self.parking_space_status}"
