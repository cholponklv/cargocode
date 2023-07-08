from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class RoleChoice:
    superuser = 'superuser'
    shipper = 'shipper'
    driver = 'driver'
    company_admin = 'company_admin'

    @classmethod
    def choices(cls):
        return (
            (cls.superuser, cls.superuser),
            (cls.shipper, cls.shipper),
            (cls.driver, cls.driver),
            (cls.company_admin, cls.company_admin),
        )

    @classmethod
    def all(cls):
        return cls.superuser, cls.shipper, cls.driver, cls.company_admin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Username field must be set')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        extra_fields.setdefault('role', RoleChoice.superuser)

        return self.create_user(email, password, **extra_fields)

class Rating(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='rating_user')
    target_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='target_user')
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        output = f'{self.user.name} rated {self.target_user.name} with {self.rating} stars'
        return output

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/avatar')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=RoleChoice.choices(), default=RoleChoice.shipper)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    def __str__(self):
        return self.id
