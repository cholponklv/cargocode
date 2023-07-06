from django.urls import path

from user import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('v1/shipper/register/', views.ShipperRegisterView.as_view(), name='shipper_register'),
    path('v1/driver/register/', views.DriverRegisterView.as_view(), name='driver_register'),
    path('v1/verify-email/', views.EmailVerificationView.as_view(), name='verify_email'),
    path('v1/login/', views.LoginApiView.as_view(), name='login'),
    path('v1/get-user/', views.GetUserView.as_view()),

]
