from django.urls import path, include
from driver import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('drivers',viewset=views.DriverViewSet, basename='drivers')
urlpatterns = [
    path('v1/', include(router.urls)),
]