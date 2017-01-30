from rest_framework import serializers
from Drives import models
from Clients.api.serializers import ParentsSerilaizer, LocationSerilaizer


class VehicleSerializer(serializers.ModelSerializer):
    parents = ParentsSerilaizer(read_only=True, many=True)

    class Meta:
        model = models.Vehicle
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True, many=True)
    location = LocationSerilaizer(read_only=True)

    class Meta:
        model = models.Driver
        fields = '__all__'
