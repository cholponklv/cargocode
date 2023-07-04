from django.urls import path, include
from . import views

from rest_framework import routers



router = routers.DefaultRouter()
router.register('truck', viewset=views.TruckViewSet, basename='trucks')
urlpatterns = [
    path('', include(router.urls)),

]

