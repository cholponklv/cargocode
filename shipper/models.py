from django.db import models

from user.models import User


# Create your models here.

class Shipper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
