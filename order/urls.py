from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()

router.register('orders', viewset=views.OrdersViewSet, basename='orders')
router.register('orderoffers', viewset=views.OrdersOfferViewSet, basename='orders')
router.register('cargotypes', viewset=views.CargoTypeViewSet, basename='cargotypes')
urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/orders/<int:pk>/offers/<int:offer_id>/accept/', views.OrdersViewSet.as_view({'post': 'accept'}), name='order-accept'),
    # path('v1/orders/<int:pk>/offers/<int:offer_id>/driver/<int:driver_id>/accept/', views.OrdersViewSet.as_view({'post': 'driver'}), name='driver'),
]
