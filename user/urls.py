from django.urls import path

from .views import RegisterUserView, LoginApiView

urlpatterns = [
    path('v1/signup/', RegisterUserView.as_view(), name='signup'),
    path('v1/login/', LoginApiView.as_view(), name='login')

]
