from django.urls import path, include
from company import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('companies', viewset=views.CompanyViewSet, basename='companies')

urlpatterns = [
    path('v1/', include(router.urls)),
]
