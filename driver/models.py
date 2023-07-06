from django.db import models

from user.models import User
from company.models import Company

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rpm = models.IntegerField()
    experience = models.IntegerField()
    rating = models.IntegerField()
    city = models.CharField(max_length=100, null=True,blank=True)
    is_available = models.BooleanField(default=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null = True,blank=True)

    def __str__(self):
        return self.user.email


class DriverDocument(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document')
    type = models.ForeignKey('driver.DocumentType', on_delete=models.CASCADE)


class DocumentType(models.Model):
    CHOICES = (
        ('company', 'company'),
        ('shipper', 'shipper'),
        ('driver', 'driver')
    )
    name = models.CharField(max_length=100)
    type = models.CharField(choices=CHOICES)
    required = models.BooleanField(default=False)
