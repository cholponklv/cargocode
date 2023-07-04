from .models import Order
from shipper.models import Shipper
from .serializers import OrderSerializer
from rest_framework import viewsets
from .permissions import IsOwner
from rest_framework import viewsets

from shipper.models import Shipper
from .models import Order
from .permissions import IsOwner
from .serializers import OrderSerializer


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
        return Order.objects.filter(shipper=shipper)
