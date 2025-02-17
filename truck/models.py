# Create your models here.
from django.db import models

from company.models import Company
from driver.models import Driver


# Create your models here.
class Truck(models.Model):
    name = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    max_load_capacity = models.DecimalField(max_digits=5, decimal_places=2)
