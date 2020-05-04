"""Addresses app models"""

from django.contrib.auth import get_user_model
from django.db import models


class Address(models.Model):
    """Address base model"""
    name = models.CharField('nombre', max_length=255)
    indoor_number = models.CharField(
        verbose_name='número interior',
        max_length=50,
        blank=True,
        null=True
    )
    latitude = models.FloatField('latitud')
    longitude = models.FloatField('longitud')

    def __str__(self):
        """Returns string representation of a address"""
        if self.indoor_number:
            return f'{self.name} ({self.indoor_number})'
        else:
            return self.name

    class Meta:
        verbose_name = 'dirección'
        verbose_name_plural = 'direcciones'


class UserAddress(Address):
    """Address for users"""
    user = models.ForeignKey(
        verbose_name='usuario',
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    alias = models.CharField('alias', max_length=50)

    class Meta:
        verbose_name = 'dirección de usuario'
        verbose_name_plural = 'direcciones de usuarios'
