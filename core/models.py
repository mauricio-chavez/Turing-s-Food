"""Core models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from checkout.utils.stripe import create_customer


class UserManager(BaseUserManager):
    """Manages user mapped objects"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.customer_id = create_customer().get('id')
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_delivery_man = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.customer_id = create_customer().id
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField('está activo', default=True)
    is_staff = models.BooleanField('es staff', default=False)
    is_superuser = models.BooleanField('es superusuario', default=False)
    is_delivery_man = models.BooleanField('es repartidor', default=False)
    is_admin = models.BooleanField('es administrador', default=False)
    customer_id = models.CharField(
        verbose_name='id de cliente de stripe',
        max_length=100,
        blank=True,
        null=True
    )
    STATUS_CHOICES = (
        ('Comensal', 1),
        ('Repartidor', 2),
        ('Administrador', 3)
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=1
    )
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'usuario'

    def get_full_name(self):
        """Concats first and last names"""
        return f'{self.first_name} {self.last_name}'
