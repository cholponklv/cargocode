from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mc = models.CharField(max_length=100)
    dot = models.CharField(max_length=100)

    def __str__(self):
        return self.name
