from rest_framework import generics
from . import serializers
from Drives import models


class ListDrivers(generics.ListAPIView):
    queryset = models.Driver.objects.all()
    serializer_class =  serializers.DriverSerializer

class ListVehicle(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer