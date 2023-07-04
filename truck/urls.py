from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('truck', viewset=views.TruckViewSet, basename='trucks')
urlpatterns = [
    path('', include(router.urls)),

]
