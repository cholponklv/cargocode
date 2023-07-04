from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()

router.register('orders', viewset=views.OrdersViewSet, basename='orders')
urlpatterns = [
    path('v1/', include(router.urls)),
]
