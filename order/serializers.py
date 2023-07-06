from rest_framework import serializers
from driver.serializers import DriverSerializer
from .models import Order, OrderOffer, CargoType
from company.serializers import CompanySerializer
from shipper.serializers import ShipperSerializer

class CargoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoType
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["cargo_type"]=CargoTypeSerializer(instance.cargo_type).data
        data["driver"]=DriverSerializer(instance.driver).data 
        data["company"]=CompanySerializer(instance.company).data 
        data["shipper"]=ShipperSerializer(instance.shipper).data 
        return data



class OrderOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOffer
        fields = '__all__'


class SelectDriverSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()