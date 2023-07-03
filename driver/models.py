from django.db import models
from user.models import User
# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField()
    rpm = models.IntegerField()
    rating = models.IntegerField()


class DriverDocument(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document')

class DocumentType(models.Model):
    document = models.OneToOneField(DriverDocument,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    