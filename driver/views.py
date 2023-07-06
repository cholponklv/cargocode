from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Driver
from shipper.models import Shipper
from .serializers import DriverSerializer
from rest_framework import generics,mixins, viewsets , filters

# Create your views here.

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.request.user)
        if user.is_staff:
            return Driver.objects.all()

        if hasattr(self.request.user, 'shipper'):
            shipper = self.request.user.shipper
            orders = shipper.order_set.filter(status='waiting')
            order_cities = orders.values_list('location_city', flat=True)

            drivers = Driver.objects.filter(
                city__in=order_cities,
                is_available=True
            )
            return drivers
        if hasattr(self.request.user, 'companyemployee'):
            employcompany = self.request.user.companyemployee.company
            drivers = Driver.objects.filter(
                company=employcompany
            )
            return drivers
        return Driver.objects.all()