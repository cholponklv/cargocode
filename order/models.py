from django.db import models

# Create your models here.
from django.db import models
from shipper.models import Shipper
from driver.models import Driver
from company.models import Company,CompanyEmployee


class CargoType(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    CHOICES = (
        ('quick', 'quick'),
        ('slow', 'slow'),
    )
    STATUS = (
        ('waiting', 'waiting'),
        ('going', 'going'),
        ('done', 'done')
    )
    cargo_type = models.ForeignKey(CargoType, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    loading_loc = models.CharField(max_length=123)
    location_city = models.CharField(max_length=123,null=True,blank=True)
    delivery_dest = models.CharField(max_length=123)
    delivery_city = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null = True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True)
    delivery_type = models.CharField(choices=CHOICES,default="slow")
    status = models.CharField(choices=STATUS,default="waiting")

    def __str__(self):
        return str(self.id)
    

class OrderOffer(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,blank=True,null=True)
    companyemployee = models.ForeignKey(CompanyEmployee, on_delete=models.CASCADE,blank=True,null=True)
    driver_price = models.IntegerField(null=True,blank=True)
    rpm = models.IntegerField(blank=True,null=True)

