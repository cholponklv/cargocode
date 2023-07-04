from django.urls import path, include
from order import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('order',viewset=views.OrdersViewSet, basename='order')
urlpatterns = [
    path('', include(router.urls)),
]