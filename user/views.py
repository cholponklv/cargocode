from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from driver.serializers import DriverSerializer
from shipper.serializers import ShipperSerializer
from user import serializers
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


def generate_confirmation_code():
    code = random.randint(100000, 999999)
    return code


def send_confirmation_email(email, code):
    subject = 'Confirmation Code'
    message = f'Your confirmation code is: {code}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])


class EmailVerificationView(generics.GenericAPIView):
    serializer_class = serializers.EmailVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')

        try:
            user = User.objects.get(verification_code=code, is_verified=False)
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid confirmation code."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.is_verified = True
        user.verification_code = None
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": serializers.UserSerializer(instance=user, context={'request': request}).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(data, status=status.HTTP_200_OK)


class ShipperRegisterView(CreateAPIView):
    serializer_class = serializers.ShipperRegisterSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shipper = serializer.save()
        user = shipper.user

        # Генерация и отправка кода подтверждения на почту
        confirmation_code = generate_confirmation_code()
        user.verification_code = confirmation_code
        user.save()

        send_confirmation_email(user.email, confirmation_code)

        # Генерация и возврат токена
        refresh = RefreshToken.for_user(user)
        data = {
            'shipper': ShipperSerializer(instance=shipper, context={'request': request}).data,
            "token": str(refresh.access_token)
        }

        return Response(data, status=status.HTTP_201_CREATED)


class DriverRegisterView(CreateAPIView):
    serializer_class = serializers.DriverRegisterSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        driver = serializer.save()
        user = driver.user

        # Генерация и отправка кода подтверждения на почту
        confirmation_code = generate_confirmation_code()
        user.verification_code = confirmation_code
        user.save()

        send_confirmation_email(user.email, confirmation_code)

        # Генерация и возврат токена
        refresh = RefreshToken.for_user(user)
        data = {
            'shipper': DriverSerializer(instance=driver, context={'request': request}).data,
            "token": str(refresh.access_token)
        }

        return Response(data, status=status.HTTP_201_CREATED)


class LoginApiView(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            raise AuthenticationFailed()
        user.last_login = timezone.now()
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": serializers.UserSerializer(instance=user, context={'request': request}).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(data=data, status=status.HTTP_200_OK)


class GetUserView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    pagination_class = None

    def get(self, request):
        return Response(data=self.get_serializer(instance=request.user).data)
