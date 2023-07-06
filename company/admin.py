from django.contrib import admin

# Register your models here.

from .models import Company,CompanyEmployee

admin.site.register(Company)
admin.site.register(CompanyEmployee)
