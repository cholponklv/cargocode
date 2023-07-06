from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()

router.register('orders', viewset=views.OrdersViewSet, basename='orders')
router.register('orderoffers', viewset=views.OrdersOfferViewSet, basename='orders')
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/orders/<int:pk>/accept/<int:offer_id>/', views.OrdersViewSet.as_view({'post': 'accept'}), name='order-accept'),
]
