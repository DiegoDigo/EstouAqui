from rest_framework import serializers
from Drives import models


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Driver
        fields = '__all__'
