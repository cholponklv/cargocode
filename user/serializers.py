from rest_framework import serializers

from company.models import Company
# Подключаем модель user
from .models import User
from shipper.models import Shipper
from driver.models import Driver


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'password', 'password2']
        write_only_fields = ('password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ShipperRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Shipper
        fields = ['user', 'company', 'billing_address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'shipper'
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        shipper = Shipper.objects.create(user=user, **validated_data)
        return shipper


class DriverRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Driver
        fields = ('user', 'experience', 'rpm')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'driver'
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        shipper = Driver.objects.create(user=user, **validated_data)
        return shipper


class CompanyEmployeeSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)

class CompanyRegisterSerializer(serializers.Serializer):
    user = UserRegisterSerializer()
    company_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    mc = serializers.CharField(max_length=100)
    dot = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'company_admin'
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        position = validated_data.pop('position')
        name = validated_data.pop('company_name')
        company = Company.objects.create(name=name, **validated_data)
        company_employee = company.companyemployee_set.create(user=user, position=position)
        return company_employee


class EmailVerificationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Confirmation code must be a numeric value.")
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number', 'email', 'role', 'is_verified')
