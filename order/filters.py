from django_filters.rest_framework import filterset
from .models import Order,OrderOffer



class OrderFilter(filterset.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'

  
class OrderOfferFilter(filterset.FilterSet):
    class Meta:
        model = OrderOffer
        fields = '__all__'

      
    
