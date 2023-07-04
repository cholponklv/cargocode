from django.urls import path, include
from .views import RegistrUserView ,LoginApiView
urlpatterns=[
    path('signup/', RegistrUserView.as_view(), name='signup'),
    path('login/', LoginApiView.as_view(), name='login')

]