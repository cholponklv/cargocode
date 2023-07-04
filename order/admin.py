from django.contrib import admin

# Register your models here.
from .models import Order,CargoType
admin.site.register(Order)
admin.site.register(CargoType)