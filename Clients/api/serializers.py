from rest_framework import serializers
from Clients import models


class LocationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class SchoolSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = '__all__'


class ChildrenSerilaizer(serializers.ModelSerializer):
    school = SchoolSerilaizer(read_only=True)

    class Meta:
        model = models.Children
        fields = '__all__'


class ParentsSerilaizer(serializers.ModelSerializer):
    location = LocationSerilaizer(read_only=True)
    children = ChildrenSerilaizer(read_only=True, many=True)

    class Meta:
        model = models.Parents
        fields = '__all__'
