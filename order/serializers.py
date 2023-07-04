from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','cargo_type','driver','company','shipper','loading_loc','delivery_dest','weight','price')
