from django.db import models
from user.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mc = models.CharField(max_length=100)
    dot = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CompanyEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return str(self.company)
