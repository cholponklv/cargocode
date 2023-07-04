from django.shortcuts import render

# Create your views here.

from .serializers import TruckSerializer
from .models import Truck
from rest_framework import viewsets

# Create your views here.
class TruckViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()