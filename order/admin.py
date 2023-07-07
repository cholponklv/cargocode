from django.contrib import admin

# Register your models here.
from .models import Order, CargoType, OrderOffer

admin.site.register(Order)
admin.site.register(OrderOffer)
admin.site.register(CargoType)
