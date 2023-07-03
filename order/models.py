from django.db import models

# Create your models here.
from django.db import models
from shipper.models import Shipper
from driver.models import Driver
from company.models import Company

# Create your models here.
class OrderType(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    loading_loc = models.CharField(max_length=123)
    delivery_dest = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=6, decimal_places=2,default=0)

