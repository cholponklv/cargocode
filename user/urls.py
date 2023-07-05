from django.urls import path

from .views import RegisterUserView, LoginApiView, GetUserView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('v1/signup/', RegisterUserView.as_view(), name='signup'),
    path('v1/login/', LoginApiView.as_view(), name='login'),
    path('v1/get-user/', GetUserView.as_view()),

]
