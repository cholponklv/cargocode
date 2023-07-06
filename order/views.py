from .models import Order
from shipper.models import Shipper
from .serializers import OrderSerializer,OrderOfferSerializer ,SelectDriverSerializer
from rest_framework import viewsets
from .permissions import IsOwner
from rest_framework import viewsets,status

from shipper.models import Shipper
from .models import Order
from .permissions import IsOwner,IsDriverFromSameCity
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from driver.models import Driver
from order.models import OrderOffer

# Create your views here.

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner|IsDriverFromSameCity]

    def get_queryset(self):
        
        if self.request.user.is_staff:
            return Order.objects.all()
        
        if hasattr(self.request.user, 'shipper'):
            shipper = self.request.user.shipper
            return Order.objects.filter(shipper=shipper)
        
        if hasattr(self.request.user, 'driver'):
            driver = self.request.user.driver
            driver_city = driver.city
            return Order.objects.filter(location_city=driver_city)
        
        return Order.objects.all()
    

    @action(detail=True, methods=['POST'])
    def offers(self, request, pk=None):
        order = self.get_object()
        user = self.request.user

        if hasattr(user, 'driver'):
            driver = user.driver


            if OrderOffer.objects.filter(order=order, driver=driver).exists():
                return Response({'error': 'Заявка уже отправлена'}, status=status.HTTP_400_BAD_REQUEST)

            order_driver = OrderOffer.objects.create(order=order, driver=driver)
            return Response({'message': 'Заявка успешно отправлена'}, status=status.HTTP_200_OK)
        return Response({'error': 'Вы не являетесь водителем'}, status=status.HTTP_403_FORBIDDEN)
    
     
    
    

    @action(detail=True, methods=['POST'], url_path='accept/(?P<offer_id>\d+)/')
    def accept(self, request, pk=None, offer_id=None):
        order = self.get_object()

        try:
            order_offer = OrderOffer.objects.get(id=offer_id, order=order)
        except OrderOffer.DoesNotExist:
            return Response({'error': 'Указан недействительный идентификатор ставки'}, status=status.HTTP_400_BAD_REQUEST)

        order.driver = order_offer.driver
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrdersOfferViewSet(viewsets.ModelViewSet):
    queryset = OrderOffer.objects.all()
    serializer_class = OrderOfferSerializer