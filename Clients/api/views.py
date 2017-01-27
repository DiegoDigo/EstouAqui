from rest_framework import generics
from . import serializers
from Clients import models


class SchoolList(generics.ListAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerilaizer


class LocationList(generics.ListAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerilaizer


class ChildrenList(generics.ListAPIView):
    queryset = models.Children.objects.all()
    serializer_class = serializers.ChildrenSerilaizer


class ParentsList(generics.ListAPIView):
    queryset = models.Parents.objects.all()
    serializer_class = serializers.ParentsSerilaizer
