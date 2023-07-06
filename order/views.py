from .models import Order
from shipper.models import Shipper
from .serializers import OrderSerializer,OrderOfferSerializer ,SelectDriverSerializer
from rest_framework import viewsets
from .permissions import IsOwner
from rest_framework import viewsets,status
from company.models import Company
from shipper.models import Shipper
from .models import Order
from .permissions import IsOwner,IsDriver ,IsCompanyEmployee
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from driver.models import Driver
from order.models import OrderOffer
from django_filters import rest_framework as dj_filters
from rest_framework import generics,mixins, viewsets, filters
from .filters import OrderFilter,OrderOfferFilter
# Create your views here.

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = OrderFilter
    ordering_fields = '__all__'
    search_fields =  ('loading_loc','loading_city','delivery_dest','delivery_city','status')
    def get_queryset(self):
        
        if self.request.user.is_staff:
            return Order.objects.all()
        
        if hasattr(self.request.user, 'shipper'):
            shipper = self.request.user.shipper
            return Order.objects.filter(shipper=shipper)
        
        return Order.objects.all()
    

    @action(detail=True, methods=['POST']   , permission_classes = [IsOwner|IsDriver|IsCompanyEmployee])
    def offers(self, request, pk=None):
        order = self.get_object()
        print(self.permission_classes)
        user = self.request.user

        if hasattr(user, 'driver'):
            driver = user.driver


            if OrderOffer.objects.filter(order=order, driver=driver).exists():
                return Response({'error': 'Заявка уже отправлена'}, status=status.HTTP_400_BAD_REQUEST)

            order_offer = OrderOffer.objects.create(order=order, driver=driver)
            return Response({'message': 'Заявка успешно отправлена'}, status=status.HTTP_200_OK)
       
    

        if hasattr(user, 'companyemployee'):
            companyemployee = user.companyemployee


            if OrderOffer.objects.filter(order=order, companyemployee=companyemployee).exists():
                return Response({'error': 'Заявка уже отправлена'}, status=status.HTTP_400_BAD_REQUEST)

            order_offer = OrderOffer.objects.create(order=order, companyemployee=companyemployee)
            return Response({'message': 'Заявка успешно отправлена'}, status=status.HTTP_200_OK)
        return Response({'error': 'У вас нет прав'}, status=status.HTTP_403_FORBIDDEN)
    
     
    
    

    @action(detail=True, methods=['POST'], url_path='offers/(?P<offer_id>\d+)/accept',permission_classes=[IsOwner])
    def accept(self, request, offer_id, pk=None):
        order = self.get_object()
        try:
            order_offer = OrderOffer.objects.get(id=offer_id, order=order)
        except OrderOffer.DoesNotExist:
            return Response({'error': 'Указан недействительный идентификатор ставки'}, status=status.HTTP_400_BAD_REQUEST)
        if order_offer.driver:
            order.driver = order_offer.driver
            if order.driver.company:
                order.company = order.driver.company
            order.status = 'going'
        if order_offer.companyemployee:
            company = Company.objects.get(name=str(order_offer.companyemployee))
            order.company = company
            order.status = 'going'
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], url_path='assign-driver/(?P<driver_id>\d+)',permission_classes=[IsCompanyEmployee])
    def assign_driver(self, request, driver_id, pk=None):
        order = self.get_object()
        if request.user.companyemployee.company != order.company:
            return Response({'error': 'Указан недействительный идентификатор компании'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            driver = Driver.objects.get(id = driver_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Указан недействительный идентификатор водителя'}, status=status.HTTP_400_BAD_REQUEST)
        if driver.company != order.company:
            return Response({'error': 'Указан недействительный идентификатор водителяя'}, status=status.HTTP_400_BAD_REQUEST)
        if driver:
            order.driver =driver
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class OrdersOfferViewSet(viewsets.ModelViewSet):
    queryset = OrderOffer.objects.all()
    serializer_class = OrderOfferSerializer
    permission_classes = [IsOwner]
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = OrderOfferFilter
    ordering_fields = '__all__'
    search_fields =  ('driver_price')