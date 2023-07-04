from django.shortcuts import render
from .models import Order
from shipper.models import Shipper
from .serializers import OrderSerializer
from rest_framework import generics,mixins, viewsets , filters
from .permissions import IsOwner
# Create your views here.

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        print(self.request.user)
        shipper = Shipper.objects.get(user=self.request.user)
        return Order.objects.filter(shipper = shipper)