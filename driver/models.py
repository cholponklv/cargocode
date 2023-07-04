from django.db import models

from user.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField()
    rpm = models.IntegerField()
    rating = models.IntegerField()

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
