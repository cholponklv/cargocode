from django.urls import path, include
from company import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('company',viewset=views.CompanyViewSet, basename='company')
urlpatterns = [
    path('', include(router.urls)),
]