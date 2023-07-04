# Create your views here.

from rest_framework import viewsets

from .models import Truck
from .serializers import TruckSerializer


# Create your views here.
class TruckViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
