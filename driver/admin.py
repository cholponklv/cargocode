from django.contrib import admin

# Register your models here.
from .models import DriverDocument, DocumentType, Driver

admin.site.register(Driver)
admin.site.register(DriverDocument)
admin.site.register(DocumentType)

