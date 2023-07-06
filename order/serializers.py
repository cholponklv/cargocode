from rest_framework import serializers

from .models import Order,OrderOffer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOffer
        fields = '__all__'


class SelectDriverSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()