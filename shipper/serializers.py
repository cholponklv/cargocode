from .models import Shipper
from rest_framework import serializers


class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'
