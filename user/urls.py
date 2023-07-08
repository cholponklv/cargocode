from django.urls import path, include

from user import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'rating', RatingViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('v1/shipper/register/', views.ShipperRegisterView.as_view(), name='shipper_register'),
    path('v1/driver/register/', views.DriverRegisterView.as_view(), name='driver_register'),
    path('v1/verify-email/', views.EmailVerificationView.as_view(), name='verify_email'),
    path('v1/login/', views.LoginApiView.as_view(), name='login'),
    path('v1/get-user/', views.GetUserView.as_view()),

    # path('v1/own-rating/', views.OwnRatingView.as_view()),
    path('v1/own-rating/', views.get_own_rating),
    

]
