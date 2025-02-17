from django.shortcuts import render
from .models import Company
from .serializers import CompanySerializer
from rest_framework import generics, mixins, viewsets, filters


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
